# Generated by Django 3.2.3 on 2021-06-16 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_headercustomisation_small_banner_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecustomisation',
            name='small_banner_text',
            field=models.TextField(default='Welcome', max_length=200),
        ),
    ]
