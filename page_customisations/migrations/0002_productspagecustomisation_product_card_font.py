# Generated by Django 3.2.3 on 2021-06-20 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productspagecustomisation',
            name='product_card_font',
            field=models.TextField(default=''),
        ),
    ]