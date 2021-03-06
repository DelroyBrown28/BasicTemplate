# Generated by Django 3.2.3 on 2021-08-03 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0020_auto_20210803_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpagecustomisation',
            name='contact_card_title',
            field=models.CharField(default='Business Name', max_length=100),
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
