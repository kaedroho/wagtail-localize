# Generated by Django 3.0.6 on 2020-07-20 17:27

import uuid

import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0057_page_locale_fields_notnull"),
        ("wagtail_localize", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Translation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("source_last_updated_at", models.DateTimeField(auto_now_add=True)),
                ("translations_last_updated_at", models.DateTimeField(null=True)),
                ("destination_last_updated_at", models.DateTimeField(null=True)),
                ("enabled", models.BooleanField(default=True)),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="wagtail_localize.TranslatableObject",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="wagtail_localize.TranslationSource",
                    ),
                ),
                (
                    "target_locale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="wagtailcore.Locale",
                    ),
                ),
            ],
            options={
                "unique_together": {("object", "target_locale")},
            },
        ),
    ]
