# Generated by Django 3.2.4 on 2021-07-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_localize", "0014_remove_translation_source_last_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="translationcontext",
            name="field_path",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
    ]
