# Generated by Django 3.2.3 on 2021-06-27 17:07

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCustomisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_styling', models.CharField(default='Default Styling', max_length=55)),
                ('header_logo', models.ImageField(blank=True, null=True, upload_to='media')),
                ('header_background_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('header_icon_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('header_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('search_icon_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('search_icon_background_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('small_banner_text', models.CharField(default='Welcome', max_length=100)),
                ('small_banner_background_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('small_banner_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('do_not_display', models.BooleanField(default=False, help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.', verbose_name='Do not display')),
            ],
            options={
                'verbose_name_plural': 'Header',
            },
        ),
        migrations.CreateModel(
            name='HomePageCustomisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_page_styling', models.CharField(default='Name This Styling...', max_length=35)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('main_page_text', models.TextField()),
                ('main_page_text_alignment', models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left')),
                ('main_page_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('button_text', models.CharField(default='Shop Now', max_length=15)),
                ('button_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('button_background_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('main_page_button_alignment', models.TextField(choices=[('text-align__center', 'Center'), ('text-align__left', 'Left'), ('text-align__right', 'Right')], default='text-align__left')),
                ('do_not_display', models.BooleanField(default=False, help_text='CHECK THIS BOX TO HIDE THIS SPECIFIC STYLING.', verbose_name='Do not display')),
            ],
            options={
                'verbose_name_plural': 'Home Page',
            },
        ),
        migrations.CreateModel(
            name='ProductsPageCustomisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_page_styling', models.CharField(default='Default Product Page Styling', max_length=55)),
                ('product_page_background_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('products_page_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('category_tag_border_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('category_tag_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('product_card_background_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('add_card_border', models.TextField(choices=[('add-border', 'Add Border'), ('no-border', 'No Border')], default='No Border')),
                ('border_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('product_card_font_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18)),
                ('product_card_icon_color', colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18)),
                ('product_quantity_buttons', colorfield.fields.ColorField(default='#FFFFFFFF', help_text='**Product Display Page', max_length=18)),
                ('keep_shopping_button_color', colorfield.fields.ColorField(default='#FFFFFFFF', help_text='**Product Display Page', max_length=18)),
                ('keep_shopping_button_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', help_text='**Product Display Page', max_length=18)),
                ('add_to_bag_button_color', colorfield.fields.ColorField(default='#FFFFFFFF', help_text='**Product Display Page', max_length=18)),
                ('add_to_bag_button_text_color', colorfield.fields.ColorField(default='#FFFFFFFF', help_text='**Product Display Page', max_length=18)),
                ('do_not_display', models.BooleanField(default=False, help_text='**Check this box to hide this specific styling.', verbose_name='Do not display')),
            ],
            options={
                'verbose_name_plural': 'Products Page',
            },
        ),
    ]
