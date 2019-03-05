# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 17:01
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0143_rm_formfieldwithbutton'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([(b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Maximum character count: 25 (including spaces)', required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Maximum character count: 185 (including spaces)', required=False)), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select to render any links given above as buttons.', required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Should be exactly 390px tall, and up to 940px wide, unless this is an overlay or bleeding style hero.', required=False)), (b'is_overlay', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select if you want the provided image to be a background image under the entire hero.', required=False)), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Specify a hex value (with the # sign) from our official palette: https://github.com/cfpb/cf-theme-cfpb/blob/master/src/color-palette.less', required=False)), (b'is_white_text', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Turns the hero text white. Useful if using a dark background color or background image.', required=False)), (b'cta_link_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'If using a dark background color or background image, you may need to specify an alternate color for the call-to-action link. Specify a hex value (with the # sign) from our official palette: https://github.com/cfpb/cf-theme-cfpb/blob/master/src/color-palette.less', label=b'CTA link color', required=False)), (b'is_bleeding', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select if you want the provided image to bleed vertically off the top and bottom of the hero.', required=False)), (b'small_image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Provide an alternate image for small displays when using a bleeding or overlay hero.', required=False))])), (b'text_introduction', wagtail.wagtailcore.blocks.StructBlock([(b'eyebrow', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional: Adds an H5 eyebrow above H1 heading text. Only use in conjunction with heading.', label=b'Pre-heading', required=False)), (b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Check this to add a horizontal rule line to bottom of text introduction.', label=b'Has bottom rule', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='sublandingfilterablepage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([(b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Maximum character count: 25 (including spaces)', required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Maximum character count: 185 (including spaces)', required=False)), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select to render any links given above as buttons.', required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Should be exactly 390px tall, and up to 940px wide, unless this is an overlay or bleeding style hero.', required=False)), (b'is_overlay', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select if you want the provided image to be a background image under the entire hero.', required=False)), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Specify a hex value (with the # sign) from our official palette: https://github.com/cfpb/cf-theme-cfpb/blob/master/src/color-palette.less', required=False)), (b'is_white_text', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Turns the hero text white. Useful if using a dark background color or background image.', required=False)), (b'cta_link_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'If using a dark background color or background image, you may need to specify an alternate color for the call-to-action link. Specify a hex value (with the # sign) from our official palette: https://github.com/cfpb/cf-theme-cfpb/blob/master/src/color-palette.less', label=b'CTA link color', required=False)), (b'is_bleeding', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select if you want the provided image to bleed vertically off the top and bottom of the hero.', required=False)), (b'small_image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Provide an alternate image for small displays when using a bleeding or overlay hero.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='sublandingpage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField([(b'hero', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Maximum character count: 25 (including spaces)', required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Maximum character count: 185 (including spaces)', required=False)), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select to render any links given above as buttons.', required=False)), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Should be exactly 390px tall, and up to 940px wide, unless this is an overlay or bleeding style hero.', required=False)), (b'is_overlay', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select if you want the provided image to be a background image under the entire hero.', required=False)), (b'background_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Specify a hex value (with the # sign) from our official palette: https://github.com/cfpb/cf-theme-cfpb/blob/master/src/color-palette.less', required=False)), (b'is_white_text', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Turns the hero text white. Useful if using a dark background color or background image.', required=False)), (b'cta_link_color', wagtail.wagtailcore.blocks.CharBlock(help_text=b'If using a dark background color or background image, you may need to specify an alternate color for the call-to-action link. Specify a hex value (with the # sign) from our official palette: https://github.com/cfpb/cf-theme-cfpb/blob/master/src/color-palette.less', label=b'CTA link color', required=False)), (b'is_bleeding', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Select if you want the provided image to bleed vertically off the top and bottom of the hero.', required=False)), (b'small_image', wagtail.wagtailimages.blocks.ImageChooserBlock(help_text=b'Provide an alternate image for small displays when using a bleeding or overlay hero.', required=False))]))], blank=True),
        ),
    ]
