# Generated by Django 2.2.7 on 2019-12-20 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize_translation_memory", "0010_delete_old_location_models"),
    ]

    operations = [
        migrations.CreateModel(
            name="RelatedObjectLocation",
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
                ("path", models.TextField()),
                ("order", models.PositiveIntegerField()),
                (
                    "object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="references",
                        to="wagtail_localize_translation_memory.TranslatableObject",
                    ),
                ),
                (
                    "revision",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtail_localize_translation_memory.TranslatableRevision",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
