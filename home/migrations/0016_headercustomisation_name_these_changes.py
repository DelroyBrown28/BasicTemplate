# Generated by Django 3.2.3 on 2021-06-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_headercustomisation_choose_text_color_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='headercustomisation',
            name='name_these_changes',
            field=models.CharField(default='Default Styling', max_length=200),
        ),
    ]
