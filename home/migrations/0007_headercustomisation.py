# Generated by Django 3.2.3 on 2021-06-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_headercustomisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderCustomisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_banner_text', models.TextField(default='Welcome', max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Header Customisation',
            },
        ),
    ]
