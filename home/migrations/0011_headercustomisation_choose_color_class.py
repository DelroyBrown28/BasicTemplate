# Generated by Django 3.2.3 on 2021-06-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_homepagecustomisation_button_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='headercustomisation',
            name='choose_color_class',
            field=models.CharField(default='Blue', max_length=15),
        ),
    ]
