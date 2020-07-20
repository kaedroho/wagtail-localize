# Generated by Django 3.0.8 on 2020-07-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0002_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='relatedobjectsegment',
            name='if_untranslated',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Wait'), (2, 'Use blank value'), (3, 'Copy Source')], default=1),
        ),
        migrations.AddField(
            model_name='stringsegment',
            name='if_untranslated',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Wait'), (2, 'Use blank value'), (3, 'Copy Source')], default=1),
        ),
        migrations.AddField(
            model_name='templatesegment',
            name='if_untranslated',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Wait'), (2, 'Use blank value'), (3, 'Copy Source')], default=1),
        ),
    ]
