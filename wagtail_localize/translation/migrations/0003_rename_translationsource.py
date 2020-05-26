# Generated by Django 3.0.6 on 2020-05-26 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize', '0006_delete_language_model'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtail_localize_translation', '0002_rename_translationcontext'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TranslatableRevision',
            new_name='TranslationSource',
        ),
        migrations.RenameField(
            model_name='translationlog',
            old_name='revision',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='relatedobjectlocation',
            old_name='revision',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='segmentlocation',
            old_name='revision',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='templatelocation',
            old_name='revision',
            new_name='source',
        ),
    ]
