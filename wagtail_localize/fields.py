from wagtail.core.fields import StreamField

# Options for TranslatableField.if_untranslated
WAIT = 1
USE_BLANK_VALUE = 2
COPY_SOURCE = 3


class BaseTranslatableField:
    def __init__(self, field_name):
        self.field_name = field_name

    def get_field(self, model):
        return model._meta.get_field(self.field_name)

    def get_value(self, obj):
        return self.get_field(obj.__class__).value_from_object(obj)

    def is_editable(self, obj):
        """
        Returns True if the field is editable on the given object
        """
        return True

    def is_translated(self, obj):
        """
        Returns True if the value of this field on the given object should be
        extracted and submitted for translation
        """
        return False

    def is_synchronized(self, obj):
        """
        Returns True if the value of this field on the given object should be
        copied when translations are created/updated
        """
        return False


class TranslatableField(BaseTranslatableField):
    """
    A field that should be translated whenever the original page changes
    """

    def __init__(self, field_name, if_untranslated=WAIT):
        self.field_name = field_name
        self.if_untranslated = if_untranslated

    def is_translated(self, obj):
        return True

    def is_synchronized(self, obj):
        # Streamfields need to be re-synchronised before translation so the structure and non-translatable content is copied over
        return isinstance(self.get_field(obj.__class__), StreamField)


class SynchronizedField(BaseTranslatableField):
    """
    A field that should always be kept in sync with the original page
    """

    def is_synchronized(self, obj):
        return self.is_editable(obj)
