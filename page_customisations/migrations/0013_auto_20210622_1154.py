# Generated by Django 3.2.3 on 2021-06-22 10:54

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0012_auto_20210622_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='productspagecustomisation',
            name='product_card_background_color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
    ]