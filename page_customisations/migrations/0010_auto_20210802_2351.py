# Generated by Django 3.2.3 on 2021-08-02 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_customisations', '0009_auto_20210802_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutpagecustomisation',
            old_name='about_blurb',
            new_name='about_section_blurb',
        ),
        migrations.RenameField(
            model_name='aboutpagecustomisation',
            old_name='about_page_content',
            new_name='about_section_content',
        ),
        migrations.RenameField(
            model_name='aboutpagecustomisation',
            old_name='bottom_image_left',
            new_name='about_section_left_image',
        ),
        migrations.RenameField(
            model_name='aboutpagecustomisation',
            old_name='page_title',
            new_name='about_section_title',
        ),
        migrations.RemoveField(
            model_name='aboutpagecustomisation',
            name='bottom_image_right',
        ),
        migrations.AddField(
            model_name='aboutpagecustomisation',
            name='contact_section_title',
            field=models.CharField(default='Contact Section Title', max_length=100),
            preserve_default=False,
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
