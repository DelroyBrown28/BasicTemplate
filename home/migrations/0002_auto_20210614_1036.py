# Generated by Django 3.2.3 on 2021-06-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageBackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='HomePageSuperuserAdmin',
        ),
    ]
