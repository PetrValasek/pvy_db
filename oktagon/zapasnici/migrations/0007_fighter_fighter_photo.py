# Generated by Django 4.2.2 on 2023-06-22 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapasnici', '0006_alter_organisation_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fighter',
            name='Fighter_photo',
            field=models.ImageField(null=True, upload_to='photo/'),
        ),
    ]
