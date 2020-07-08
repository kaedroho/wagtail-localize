# Generated by Django 3.0.6 on 2020-07-08 12:57

from django.db import migrations


def populate_translationsource_specific_content_type(apps, schema_editor):
    TranslationSource = apps.get_model('wagtail_localize_translation.TranslationSource')

    for source in TranslationSource.objects.all().select_related('object').iterator():
        source.specific_content_type_id = source.object.content_type_id
        source.save(update_fields=['specific_content_type_id'])


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_translation', '0006_translationsource_specific_content_type'),
    ]

    operations = [
        migrations.RunPython(populate_translationsource_specific_content_type, migrations.RunPython.noop),
    ]
