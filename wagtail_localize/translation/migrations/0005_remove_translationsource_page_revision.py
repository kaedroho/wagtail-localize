# Generated by Django 3.0.6 on 2020-07-08 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_translation', '0004_segmenttranslation_locale_related_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translationsource',
            name='page_revision',
        ),
    ]
