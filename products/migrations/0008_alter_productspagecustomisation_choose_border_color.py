# Generated by Django 3.2.3 on 2021-06-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_productspagecustomisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productspagecustomisation',
            name='choose_border_color',
            field=models.CharField(choices=[('add-border__red', 'Red'), ('add-border__blue', 'Blue'), ('add-border__green', 'Green'), ('add-border__black', 'Black'), ('add-border__white', 'White'), ('no-border', 'No Border')], default='No Border', max_length=30),
        ),
    ]