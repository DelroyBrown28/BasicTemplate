# Generated by Django 3.2.3 on 2021-06-20 15:04

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0008_headercustomisation_search_icon_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='button_background_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='button_text_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='do_not_display',
            field=models.BooleanField(default=False, help_text='Check this box to hide this specific styling.', verbose_name='Do not display'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]
