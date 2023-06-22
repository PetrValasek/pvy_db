# Generated by Django 4.2.2 on 2023-06-22 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zapasnici', '0014_remove_organisation_organisation_networth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='organisation_fkey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zapasnici.tournaments', verbose_name='Organizace'),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='tournament_attendance',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Největší návštěvnost organizace'),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='tournament_mainfight',
            field=models.CharField(help_text='Hlavní zápas + výherce', max_length=80, null=True, verbose_name='Hlavní zápas'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_short',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Zadejte zkratku společnosti'),
        ),
    ]