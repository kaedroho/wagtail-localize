import json
import uuid

from django.contrib.contenttypes.models import ContentType
from django.db import models, transaction
from django.db.models import Subquery, OuterRef


def pk(obj):
    if isinstance(obj, models.Model):
        return obj.pk
    else:
        return obj


class TranslatableObjectManager(models.Manager):
    def get_or_create_from_instance(self, instance):
        return self.get_or_create(
            translation_key=instance.translation_key,
            content_type=ContentType.objects.get_for_model(
                instance.get_translation_model()
            ),
        )


class TranslatableObject(models.Model):
    """
    Represents something that can be translated.

    Note that one instance of this represents all translations for the object.
    """

    translation_key = models.UUIDField(primary_key=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="+"
    )

    objects = TranslatableObjectManager()

    def get_instance(self, locale):
        return self.content_type.get_object_for_this_type(
            translation_key=self.translation_key, locale=locale
        )

    class Meta:
        unique_together = [("content_type", "translation_key")]


class TranslatableRevision(models.Model):
    """
    A piece of content that to be used as a source for translations.
    """

    object = models.ForeignKey(
        TranslatableObject, on_delete=models.CASCADE, related_name="revisions"
    )
    locale = models.ForeignKey("wagtail_localize.Locale", on_delete=models.CASCADE)
    content_json = models.TextField()
    created_at = models.DateTimeField()

    page_revision = models.OneToOneField(
        "wagtailcore.PageRevision",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wagtaillocalize_revision",
    )

    def as_instance(self):
        if self.page_revision is not None:
            return self.page_revision.as_page_object()

        raise NotImplementedError(
            "revisions of non-page objects not currently supported"
        )


class SegmentQuerySet(models.QuerySet):
    def annotate_translation(self, language):
        """
        Adds a 'translation' field to the segments containing the
        text content of the segment translated into the specified
        language.
        """
        return self.annotate(
            translation=Subquery(
                SegmentTranslation.objects.filter(
                    translation_of_id=OuterRef("pk"), language_id=pk(language)
                ).values("text")
            )
        )


class Segment(models.Model):
    UUID_NAMESPACE = uuid.UUID("59ed7d1c-7eb5-45fa-9c8b-7a7057ed56d7")

    language = models.ForeignKey("wagtail_localize.Language", on_delete=models.CASCADE)
    text_id = models.UUIDField()
    text = models.TextField()

    objects = SegmentQuerySet.as_manager()

    @classmethod
    def get_text_id(cls, text):
        return uuid.uuid5(cls.UUID_NAMESPACE, text)

    @classmethod
    def from_text(cls, language, text):
        segment, created = cls.objects.get_or_create(
            language_id=pk(language),
            text_id=cls.get_text_id(text),
            defaults={"text": text},
        )

        return segment

    def save(self, *args, **kwargs):
        if self.text and self.text_id is None:
            self.text_id = self.get_text_id(self.text)

        return super().save(*args, **kwargs)

    class Meta:
        unique_together = [("language", "text_id")]


class SegmentTranslation(models.Model):
    translation_of = models.ForeignKey(
        Segment, on_delete=models.CASCADE, related_name="translations"
    )
    language = models.ForeignKey("wagtail_localize.Language", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [("language", "translation_of")]

    @classmethod
    def from_text(cls, translation_of, language, text):
        segment, created = cls.objects.get_or_create(
            translation_of=translation_of,
            language_id=pk(language),
            defaults={"text": text},
        )

        return segment


class Template(models.Model):
    BASE_UUID_NAMESPACE = uuid.UUID("4599eabc-3f8e-41a9-be61-95417d26a8cd")

    uuid = models.UUIDField(unique=True)
    template = models.TextField()
    template_format = models.CharField(max_length=100)
    segment_count = models.PositiveIntegerField()

    @classmethod
    def from_template_value(cls, template_value):
        uuid_namespace = uuid.uuid5(cls.BASE_UUID_NAMESPACE, template_value.format)

        template, created = cls.objects.get_or_create(
            uuid=uuid.uuid5(uuid_namespace, template_value.template),
            defaults={
                "template": template_value.template,
                "template_format": template_value.format,
                "segment_count": template_value.segment_count,
            },
        )

        return template


class BaseLocation(models.Model):
    revision = models.ForeignKey(TranslatableRevision, on_delete=models.CASCADE)
    path = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True


class SegmentLocationQuerySet(models.QuerySet):
    def annotate_translation(self, language):
        """
        Adds a 'translation' field to the segments containing the
        text content of the segment translated into the specified
        language.
        """
        return self.annotate(
            translation=Subquery(
                SegmentTranslation.objects.filter(
                    translation_of_id=OuterRef("segment_id"), language_id=pk(language)
                ).values("text")
            )
        )


class SegmentLocation(BaseLocation):
    segment = models.ForeignKey(
        Segment, on_delete=models.CASCADE, related_name="locations"
    )

    # When we extract the segment, we replace HTML attributes with id tags
    # The attributes that were removed are stored here. These must be
    # added into the translated strings.
    # These are stored as a mapping of element ids to KV mappings of
    # attributes in JSON format. For example:
    #
    #  For this segment: <a id="a1">Link to example.com</a>
    #
    #  The value of this field could be:
    #
    #  {
    #      "a#a1": {
    #          "href": "https://www.example.com"
    #      }
    #  }
    html_attrs = models.TextField(blank=True)

    objects = SegmentLocationQuerySet.as_manager()

    @classmethod
    def from_segment_value(cls, revision, language, segment_value):
        segment = Segment.from_text(language, segment_value.html_with_ids)

        segment_loc, created = cls.objects.get_or_create(
            revision_id=pk(revision),
            path=segment_value.path,
            order=segment_value.order,
            segment=segment,
            html_attrs=json.dumps(segment_value.get_html_attrs()),
        )

        return segment_loc


class TemplateLocation(BaseLocation):
    template = models.ForeignKey(
        Template, on_delete=models.CASCADE, related_name="locations"
    )

    @classmethod
    def from_template_value(cls, revision, template_value):
        template = Template.from_template_value(template_value)

        template_loc, created = cls.objects.get_or_create(
            revision_id=pk(revision),
            path=template_value.path,
            order=template_value.order,
            template=template,
        )

        return template_loc
