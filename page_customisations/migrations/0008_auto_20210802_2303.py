# Generated by Django 3.2.3 on 2021-08-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0007_auto_20210802_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpagecustomisation',
            name='bottom_image_left',
            field=models.ImageField(blank=True, null=True, upload_to='media/about_page_images'),
        ),
        migrations.AddField(
            model_name='aboutpagecustomisation',
            name='bottom_image_right',
            field=models.ImageField(blank=True, null=True, upload_to='media/about_page_images'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__right', 'Right'), ('text-align__center', 'Center'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__right', 'Right'), ('text-align__center', 'Center'), ('text-align__left', 'Left')], default='text-align__left'),
        ),
    ]
