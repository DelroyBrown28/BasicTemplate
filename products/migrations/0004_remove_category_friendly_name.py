# Generated by Django 3.2.3 on 2021-06-10 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_friendly_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='friendly_name',
        ),
    ]