# Generated by Django 3.1.6 on 2021-02-17 09:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks
import wagtail_localize.test.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_localize_test', '0013_pagewithcustomedithandler_pagewithcustomedithandlerchildobject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testgeneratetranslatablefieldspage',
            name='test_streamfield',
            field=wagtail.core.fields.StreamField([('test_charblock', wagtail.core.blocks.CharBlock(max_length=255)), ('test_textblock', wagtail.core.blocks.TextBlock(label='text block')), ('test_emailblock', wagtail.core.blocks.EmailBlock()), ('test_urlblock', wagtail.core.blocks.URLBlock()), ('test_richtextblock', wagtail.core.blocks.RichTextBlock()), ('test_rawhtmlblock', wagtail.core.blocks.RawHTMLBlock()), ('test_blockquoteblock', wagtail.core.blocks.BlockQuoteBlock()), ('test_structblock', wagtail.core.blocks.StructBlock([('field_a', wagtail.core.blocks.TextBlock()), ('field_b', wagtail.core.blocks.TextBlock())])), ('test_listblock', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock())), ('test_nestedstreamblock', wagtail.core.blocks.StreamBlock([('block_a', wagtail.core.blocks.TextBlock()), ('block_b', wagtail.core.blocks.TextBlock())])), ('test_customstructblock', wagtail.core.blocks.StructBlock([('field_a', wagtail.core.blocks.TextBlock()), ('field_b', wagtail.core.blocks.TextBlock())])), ('test_customblockwithoutextractmethod', wagtail_localize.test.models.CustomBlockWithoutExtractMethod()), ('test_pagechooserblock', wagtail.core.blocks.PageChooserBlock()), ('test_pagechooserblock_with_restricted_types', wagtail.core.blocks.PageChooserBlock(['wagtail_localize_test.TestHomePage', 'wagtail_localize_test.TestPage'])), ('test_imagechooserblock', wagtail.images.blocks.ImageChooserBlock()), ('test_documentchooserblock', wagtail.documents.blocks.DocumentChooserBlock()), ('test_snippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(wagtail_localize.test.models.TestSnippet)), ('test_nontranslatablesnippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(wagtail_localize.test.models.NonTranslatableSnippet)), ('test_embedblock', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='testpage',
            name='test_streamfield',
            field=wagtail.core.fields.StreamField([('test_charblock', wagtail.core.blocks.CharBlock(max_length=255)), ('test_textblock', wagtail.core.blocks.TextBlock(label='text block')), ('test_emailblock', wagtail.core.blocks.EmailBlock()), ('test_urlblock', wagtail.core.blocks.URLBlock()), ('test_richtextblock', wagtail.core.blocks.RichTextBlock()), ('test_rawhtmlblock', wagtail.core.blocks.RawHTMLBlock()), ('test_blockquoteblock', wagtail.core.blocks.BlockQuoteBlock()), ('test_structblock', wagtail.core.blocks.StructBlock([('field_a', wagtail.core.blocks.TextBlock()), ('field_b', wagtail.core.blocks.TextBlock())])), ('test_listblock', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock())), ('test_nestedstreamblock', wagtail.core.blocks.StreamBlock([('block_a', wagtail.core.blocks.TextBlock()), ('block_b', wagtail.core.blocks.TextBlock())])), ('test_customstructblock', wagtail.core.blocks.StructBlock([('field_a', wagtail.core.blocks.TextBlock()), ('field_b', wagtail.core.blocks.TextBlock())])), ('test_customblockwithoutextractmethod', wagtail_localize.test.models.CustomBlockWithoutExtractMethod()), ('test_pagechooserblock', wagtail.core.blocks.PageChooserBlock()), ('test_pagechooserblock_with_restricted_types', wagtail.core.blocks.PageChooserBlock(['wagtail_localize_test.TestHomePage', 'wagtail_localize_test.TestPage'])), ('test_imagechooserblock', wagtail.images.blocks.ImageChooserBlock()), ('test_documentchooserblock', wagtail.documents.blocks.DocumentChooserBlock()), ('test_snippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(wagtail_localize.test.models.TestSnippet)), ('test_nontranslatablesnippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(wagtail_localize.test.models.NonTranslatableSnippet)), ('test_embedblock', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='testpage',
            name='test_synchronized_streamfield',
            field=wagtail.core.fields.StreamField([('test_charblock', wagtail.core.blocks.CharBlock(max_length=255)), ('test_textblock', wagtail.core.blocks.TextBlock(label='text block')), ('test_emailblock', wagtail.core.blocks.EmailBlock()), ('test_urlblock', wagtail.core.blocks.URLBlock()), ('test_richtextblock', wagtail.core.blocks.RichTextBlock()), ('test_rawhtmlblock', wagtail.core.blocks.RawHTMLBlock()), ('test_blockquoteblock', wagtail.core.blocks.BlockQuoteBlock()), ('test_structblock', wagtail.core.blocks.StructBlock([('field_a', wagtail.core.blocks.TextBlock()), ('field_b', wagtail.core.blocks.TextBlock())])), ('test_listblock', wagtail.core.blocks.ListBlock(wagtail.core.blocks.TextBlock())), ('test_nestedstreamblock', wagtail.core.blocks.StreamBlock([('block_a', wagtail.core.blocks.TextBlock()), ('block_b', wagtail.core.blocks.TextBlock())])), ('test_customstructblock', wagtail.core.blocks.StructBlock([('field_a', wagtail.core.blocks.TextBlock()), ('field_b', wagtail.core.blocks.TextBlock())])), ('test_customblockwithoutextractmethod', wagtail_localize.test.models.CustomBlockWithoutExtractMethod()), ('test_pagechooserblock', wagtail.core.blocks.PageChooserBlock()), ('test_pagechooserblock_with_restricted_types', wagtail.core.blocks.PageChooserBlock(['wagtail_localize_test.TestHomePage', 'wagtail_localize_test.TestPage'])), ('test_imagechooserblock', wagtail.images.blocks.ImageChooserBlock()), ('test_documentchooserblock', wagtail.documents.blocks.DocumentChooserBlock()), ('test_snippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(wagtail_localize.test.models.TestSnippet)), ('test_nontranslatablesnippetchooserblock', wagtail.snippets.blocks.SnippetChooserBlock(wagtail_localize.test.models.NonTranslatableSnippet)), ('test_embedblock', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
    ]
