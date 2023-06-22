# Generated by Django 4.2.2 on 2023-06-22 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zapasnici', '0015_organisation_organisation_fkey_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ['-organisation_name'], 'verbose_name': 'Organizace', 'verbose_name_plural': 'Organizace'},
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='organisation_Max_popularity',
        ),
        migrations.AlterField(
            model_name='fighter',
            name='Fighter_Height',
            field=models.PositiveIntegerField(blank=True, default=180, verbose_name='Výška zápasníka v cm'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='Fighter_description',
            field=models.PositiveIntegerField(default=20, verbose_name='Věk zápasníka'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='Fighter_score_Losses',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Počet proher'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='Fighter_score_Win',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Počet výher'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='fighter_fighting_year',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='Počet let, od započatí tréninku', null=True, verbose_name='Celkové počet let'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_fkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zapasnici.tournaments', verbose_name='Největší turnaj'),
        ),
    ]
