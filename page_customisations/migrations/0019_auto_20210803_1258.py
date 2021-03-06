# Generated by Django 3.2.3 on 2021-08-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0018_auto_20210803_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpagecustomisation',
            old_name='contact_section_info',
            new_name='contact_card_info',
        ),
        migrations.AddField(
            model_name='aboutpagecustomisation',
            name='contact_card_title',
            field=models.TextField(default='Short blurb', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_button_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
        migrations.AlterField(
            model_name='homepagecustomisation',
            name='main_page_text_alignment',
            field=models.TextField(choices=[('text-align__left', 'Left'), ('text-align__right', 'Right'), ('text-align__center', 'Center')], default='text-align__left'),
        ),
    ]
