# Generated by Django 3.1 on 2020-08-28 10:00

import django.db.models.deletion

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_localize", "0009_stringtranslation_errors"),
    ]

    operations = [
        migrations.CreateModel(
            name="OverridableSegment",
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
                ("order", models.PositiveIntegerField()),
                ("data_json", models.TextField()),
                (
                    "context",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="wagtail_localize.translationcontext",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtail_localize.translationsource",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
