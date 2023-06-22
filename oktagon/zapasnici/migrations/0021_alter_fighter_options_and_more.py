# Generated by Django 4.2.2 on 2023-06-22 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapasnici', '0020_remove_fighter_fighter_sponsors'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fighter',
            options={'ordering': ['-Fighter_id'], 'verbose_name': 'Zápasník', 'verbose_name_plural': 'Zápasníci'},
        ),
        migrations.RenameField(
            model_name='fighter',
            old_name='figher_networth',
            new_name='Figher_networth',
        ),
        migrations.RenameField(
            model_name='fighter',
            old_name='fighter_fighting_year',
            new_name='Fighter_fighting_year',
        ),
        migrations.RenameField(
            model_name='fighter',
            old_name='fighter_organisation',
            new_name='Fighter_organisation',
        ),
    ]