# Generated by Django 4.2.2 on 2023-06-22 02:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapasnici', '0005_alter_sponsors_support_money'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organisation',
            options={'ordering': ['-organisation_Max_popularity'], 'verbose_name': 'Organizace', 'verbose_name_plural': 'Organizace'},
        ),
        migrations.RemoveField(
            model_name='fighter',
            name='fighter_year',
        ),
        migrations.AddField(
            model_name='fighter',
            name='Fighter_description',
            field=models.PositiveIntegerField(default=20, max_length=2, verbose_name='Věk zápasníka'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='Fighter_email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AddField(
            model_name='fighter',
            name='Fighter_score_Losses',
            field=models.PositiveIntegerField(blank=True, default=0, max_length=2, null=True, verbose_name='Počet proher'),
        ),
        migrations.AddField(
            model_name='fighter',
            name='Fighter_score_Win',
            field=models.PositiveIntegerField(blank=True, default=0, max_length=2, null=True, verbose_name='Počet výher'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='organisation_Max_popularity',
            field=models.PositiveIntegerField(default=1000, help_text='Zadejte, Největší návštěvnost organizace', verbose_name='Popularita'),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='tournament_timeline',
            field=models.BooleanField(choices=[(True, 'Konalo se'), (False, 'Bude se konat')], default=True),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='Fighter_id',
            field=models.CharField(max_length=60, verbose_name='Jméno a příjmení'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='figher_networth',
            field=models.FloatField(blank=True, default=1000, help_text='Finanční kapitál v $', max_length=10, null=True, verbose_name='Celkové jmění'),
        ),
        migrations.AlterField(
            model_name='fighter',
            name='fighter_fighting_year',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='Počet let, od započatí tréninku', max_length=2, null=True, verbose_name='Celkové počet let'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_Median_popularity',
            field=models.PositiveIntegerField(default=1000, help_text='Zadejte, medián počtu návštěvnosti organizace', verbose_name='Popularita'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_NetWorth',
            field=models.FloatField(default=100000, help_text='NetWorth v $', verbose_name='NetWorth'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_residence',
            field=models.CharField(help_text='Zadejte, kde organizace sídlí - Země, Město', max_length=80, verbose_name='Sídlo'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_year',
            field=models.PositiveIntegerField(default=2016, help_text='Zadejte rok založení společnosti', verbose_name='Rok'),
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='support_money',
            field=models.FloatField(default=1000, help_text='Finanční částka v $', verbose_name='Finanční částka'),
        ),
        migrations.AlterField(
            model_name='sponsors',
            name='support_text',
            field=models.TextField(blank=True, help_text='Blizší specifikace partnerství', max_length=400, null=True, verbose_name='Bližší specifikace sponzorství'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='tournament_description',
            field=models.TextField(blank=True, help_text='Stručný popis turnaje', max_length=400, null=True, verbose_name='Turnaj'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='tournament_id',
            field=models.CharField(help_text='Název turnaje/akce/id', max_length=80, verbose_name='Turnaj'),
        ),
    ]
