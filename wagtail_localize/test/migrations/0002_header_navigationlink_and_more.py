from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid
import wagtail.core.blocks
import wagtail.core.blocks.field_block
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtail_localize.test.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize_test", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Header",
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
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                ("name", models.CharField(max_length=100, null=True)),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
        migrations.CreateModel(
            name="NavigationLink",
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
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("label", models.CharField(max_length=255)),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "snippet",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="navigation_links",
                        to="wagtail_localize_test.header",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
        migrations.AlterField(
            model_name="testgeneratetranslatablefieldspage",
            name="test_streamfield",
            field=wagtail.core.fields.StreamField(
                [
                    ("test_charblock", wagtail.core.blocks.CharBlock(max_length=255)),
                    (
                        "test_textblock",
                        wagtail.core.blocks.TextBlock(label="text block"),
                    ),
                    ("test_emailblock", wagtail.core.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.core.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.core.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.core.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.core.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock()),
                    ),
                    (
                        "test_listblock_in_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.field_block.CharBlock
                                    ),
                                ),
                                (
                                    "links_list",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.core.blocks.CharBlock(
                                                        blank=True,
                                                        label="List Heading",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "pages",
                                                    wagtail.core.blocks.ListBlock(
                                                        wagtail.core.blocks.PageChooserBlock()
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.core.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.core.blocks.TextBlock()),
                                ("block_b", wagtail.core.blocks.TextBlock()),
                                (
                                    "block_l",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock()
                                    ),
                                ),
                                ("chooser", wagtail.core.blocks.PageChooserBlock()),
                                (
                                    "chooser_in_struct",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            )
                                        ]
                                    ),
                                ),
                                (
                                    "chooser_in_list",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_streamblock_in_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "nested_stream",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            ),
                                            (
                                                "checklist",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customblockwithoutextractmethod",
                        wagtail_localize.test.models.CustomBlockWithoutExtractMethod(),
                    ),
                    ("test_pagechooserblock", wagtail.core.blocks.PageChooserBlock()),
                    (
                        "test_pagechooserblock_with_restricted_types",
                        wagtail.core.blocks.PageChooserBlock(
                            [
                                "wagtail_localize_test.TestHomePage",
                                "wagtail_localize_test.TestPage",
                            ]
                        ),
                    ),
                    (
                        "test_imagechooserblock",
                        wagtail.images.blocks.ImageChooserBlock(),
                    ),
                    (
                        "test_documentchooserblock",
                        wagtail.documents.blocks.DocumentChooserBlock(),
                    ),
                    (
                        "test_snippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.TestSnippet
                        ),
                    ),
                    (
                        "test_nontranslatablesnippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.NonTranslatableSnippet
                        ),
                    ),
                    ("test_embedblock", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "test_chooserstructblock",
                        wagtail.core.blocks.StructBlock(
                            [("page", wagtail.core.blocks.PageChooserBlock())]
                        ),
                    ),
                    (
                        "test_nestedchooserstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "nested_page",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="testpage",
            name="test_streamfield",
            field=wagtail.core.fields.StreamField(
                [
                    ("test_charblock", wagtail.core.blocks.CharBlock(max_length=255)),
                    (
                        "test_textblock",
                        wagtail.core.blocks.TextBlock(label="text block"),
                    ),
                    ("test_emailblock", wagtail.core.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.core.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.core.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.core.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.core.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock()),
                    ),
                    (
                        "test_listblock_in_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.field_block.CharBlock
                                    ),
                                ),
                                (
                                    "links_list",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.core.blocks.CharBlock(
                                                        blank=True,
                                                        label="List Heading",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "pages",
                                                    wagtail.core.blocks.ListBlock(
                                                        wagtail.core.blocks.PageChooserBlock()
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.core.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.core.blocks.TextBlock()),
                                ("block_b", wagtail.core.blocks.TextBlock()),
                                (
                                    "block_l",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock()
                                    ),
                                ),
                                ("chooser", wagtail.core.blocks.PageChooserBlock()),
                                (
                                    "chooser_in_struct",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            )
                                        ]
                                    ),
                                ),
                                (
                                    "chooser_in_list",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_streamblock_in_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "nested_stream",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            ),
                                            (
                                                "checklist",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customblockwithoutextractmethod",
                        wagtail_localize.test.models.CustomBlockWithoutExtractMethod(),
                    ),
                    ("test_pagechooserblock", wagtail.core.blocks.PageChooserBlock()),
                    (
                        "test_pagechooserblock_with_restricted_types",
                        wagtail.core.blocks.PageChooserBlock(
                            [
                                "wagtail_localize_test.TestHomePage",
                                "wagtail_localize_test.TestPage",
                            ]
                        ),
                    ),
                    (
                        "test_imagechooserblock",
                        wagtail.images.blocks.ImageChooserBlock(),
                    ),
                    (
                        "test_documentchooserblock",
                        wagtail.documents.blocks.DocumentChooserBlock(),
                    ),
                    (
                        "test_snippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.TestSnippet
                        ),
                    ),
                    (
                        "test_nontranslatablesnippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.NonTranslatableSnippet
                        ),
                    ),
                    ("test_embedblock", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "test_chooserstructblock",
                        wagtail.core.blocks.StructBlock(
                            [("page", wagtail.core.blocks.PageChooserBlock())]
                        ),
                    ),
                    (
                        "test_nestedchooserstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "nested_page",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
        migrations.AlterField(
            model_name="testpage",
            name="test_synchronized_streamfield",
            field=wagtail.core.fields.StreamField(
                [
                    ("test_charblock", wagtail.core.blocks.CharBlock(max_length=255)),
                    (
                        "test_textblock",
                        wagtail.core.blocks.TextBlock(label="text block"),
                    ),
                    ("test_emailblock", wagtail.core.blocks.EmailBlock()),
                    ("test_urlblock", wagtail.core.blocks.URLBlock()),
                    ("test_richtextblock", wagtail.core.blocks.RichTextBlock()),
                    ("test_rawhtmlblock", wagtail.core.blocks.RawHTMLBlock()),
                    ("test_blockquoteblock", wagtail.core.blocks.BlockQuoteBlock()),
                    (
                        "test_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_listblock",
                        wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock()),
                    ),
                    (
                        "test_listblock_in_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(required=False),
                                ),
                                (
                                    "items",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.field_block.CharBlock
                                    ),
                                ),
                                (
                                    "links_list",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "heading",
                                                    wagtail.core.blocks.CharBlock(
                                                        blank=True,
                                                        label="List Heading",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "pages",
                                                    wagtail.core.blocks.ListBlock(
                                                        wagtail.core.blocks.PageChooserBlock()
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_nestedstreamblock",
                        wagtail.core.blocks.StreamBlock(
                            [
                                ("block_a", wagtail.core.blocks.TextBlock()),
                                ("block_b", wagtail.core.blocks.TextBlock()),
                                (
                                    "block_l",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.CharBlock()
                                    ),
                                ),
                                ("chooser", wagtail.core.blocks.PageChooserBlock()),
                                (
                                    "chooser_in_struct",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            )
                                        ]
                                    ),
                                ),
                                (
                                    "chooser_in_list",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.PageChooserBlock()
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "test_streamblock_in_structblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "nested_stream",
                                    wagtail.core.blocks.StreamBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            ),
                                            (
                                                "checklist",
                                                wagtail.core.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.core.blocks.PageChooserBlock(),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "test_customstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                ("field_a", wagtail.core.blocks.TextBlock()),
                                ("field_b", wagtail.core.blocks.TextBlock()),
                            ]
                        ),
                    ),
                    (
                        "test_customblockwithoutextractmethod",
                        wagtail_localize.test.models.CustomBlockWithoutExtractMethod(),
                    ),
                    ("test_pagechooserblock", wagtail.core.blocks.PageChooserBlock()),
                    (
                        "test_pagechooserblock_with_restricted_types",
                        wagtail.core.blocks.PageChooserBlock(
                            [
                                "wagtail_localize_test.TestHomePage",
                                "wagtail_localize_test.TestPage",
                            ]
                        ),
                    ),
                    (
                        "test_imagechooserblock",
                        wagtail.images.blocks.ImageChooserBlock(),
                    ),
                    (
                        "test_documentchooserblock",
                        wagtail.documents.blocks.DocumentChooserBlock(),
                    ),
                    (
                        "test_snippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.TestSnippet
                        ),
                    ),
                    (
                        "test_nontranslatablesnippetchooserblock",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            wagtail_localize.test.models.NonTranslatableSnippet
                        ),
                    ),
                    ("test_embedblock", wagtail.embeds.blocks.EmbedBlock()),
                    (
                        "test_chooserstructblock",
                        wagtail.core.blocks.StructBlock(
                            [("page", wagtail.core.blocks.PageChooserBlock())]
                        ),
                    ),
                    (
                        "test_nestedchooserstructblock",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "nested_page",
                                    wagtail.core.blocks.StructBlock(
                                        [
                                            (
                                                "page",
                                                wagtail.core.blocks.PageChooserBlock(),
                                            )
                                        ]
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
            ),
        ),
        migrations.CreateModel(
            name="SubNavigationLink",
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
                (
                    "translation_key",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("label", models.CharField(max_length=255)),
                (
                    "locale",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="wagtailcore.locale",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "sub_nav",
                    modelcluster.fields.ParentalKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_navigation_links",
                        to="wagtail_localize_test.navigationlink",
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("translation_key", "locale")},
            },
        ),
    ]
