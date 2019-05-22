import uuid

from django.db import models, transaction


class Segment(models.Model):
    UUID_NAMESPACE = uuid.UUID('59ed7d1c-7eb5-45fa-9c8b-7a7057ed56d7')

    locale = models.ForeignKey('wagtail_translation.Locale', on_delete=models.CASCADE)
    uuid = models.UUIDField(unique=True)
    text = models.TextField()

    @classmethod
    def from_text(cls, locale, text):
        segment, created = cls.objects.get_or_create(
            locale=locale,
            uuid=uuid.uuid5(cls.UUID_NAMESPACE, text),
            defaults={
                'text': text,
            }
        )

        return segment


class SegmentTranslation(models.Model):
    translation_of = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='translations')
    locale = models.ForeignKey('wagtail_translation.Locale', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        unique_together = [
            ('locale', 'translation_of'),
        ]

    @classmethod
    def from_text(cls, translation_of, locale, text):
        segment, created = cls.objects.get_or_create(
            translation_of=translation_of,
            locale=locale,
            defaults={
                'text': text,
            }
        )

        return segment


class Template(models.Model):
    BASE_UUID_NAMESPACE = uuid.UUID('4599eabc-3f8e-41a9-be61-95417d26a8cd')

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
                'template': template_value.template,
                'template_format': template_value.format,
                'segment_count': template_value.segment_count,
            }
        )

        return template


class BasePageLocation(models.Model):
    page_revision = models.ForeignKey('wagtailcore.PageRevision', on_delete=models.CASCADE)
    path = models.TextField()

    class Meta:
        abstract = True


class SegmentPageLocation(BasePageLocation):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE, related_name='page_locations')

    @classmethod
    def from_segment_value(cls, page_revision, segment_value):
        segment = Segment.from_text(page_revision.page.locale, segment_value.text)

        segment_page_loc, created = cls.objects.get_or_create(
            page_revision=page_revision,
            path=segment_value.path,
            segment=segment,
        )

        return segment_page_loc


class TemplatePageLocation(BasePageLocation):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name='page_locations')

    @classmethod
    def from_template_value(cls, page_revision, template_value):
        template = Template.from_template_value(template_value)

        template_page_loc, created = cls.objects.get_or_create(
            page_revision=page_revision,
            path=template_value.path,
            template=template,
        )

        return template_page_loc
