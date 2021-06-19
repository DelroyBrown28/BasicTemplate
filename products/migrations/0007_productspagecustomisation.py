# Generated by Django 3.2.3 on 2021-06-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_friendly_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsPageCustomisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_these_changes', models.CharField(default='Default Product Page Styling', max_length=200)),
                ('choose_border_color', models.CharField(choices=[('add-border__red', 'Red'), ('add-border__blue', 'Blue'), ('add-border__green', 'Green'), ('no-border', 'No Border')], default='No Border', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Products Page Customisation',
            },
        ),
    ]