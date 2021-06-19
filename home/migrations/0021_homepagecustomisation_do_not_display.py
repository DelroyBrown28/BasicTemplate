# Generated by Django 3.2.3 on 2021-06-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_homepagecustomisation_main_page_text_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagecustomisation',
            name='do_not_display',
            field=models.BooleanField(default=False, help_text='Check this box to hide this specific theme.', verbose_name='Hide Theme'),
        ),
    ]