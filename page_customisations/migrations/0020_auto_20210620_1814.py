# Generated by Django 3.2.3 on 2021-06-20 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0019_rename_add_border_to_product_cards_productspagecustomisation_add_card_border'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headercustomisation',
            name='header_styling',
            field=models.CharField(default='Default Styling', max_length=55),
        ),
        migrations.AlterField(
            model_name='productspagecustomisation',
            name='add_card_border',
            field=models.TextField(choices=[('add-border', 'Add Border'), ('no-border', 'No Border')], default='No Border', max_length=55),
        ),
        migrations.AlterField(
            model_name='productspagecustomisation',
            name='products_page_styling',
            field=models.CharField(default='Default Product Page Styling', max_length=55),
        ),
    ]
