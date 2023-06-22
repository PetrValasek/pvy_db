# Generated by Django 4.2.2 on 2023-06-22 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapasnici', '0010_remove_organisation_organisation_median_popularity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='organisation_Max_payperview',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Nejvíc prodaných Payperview'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_Average_payperview',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Průměrný počet prodaných payperview'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_Max_popularity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Největší návštěvnost organizace'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='organisation_average_popularity',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Průměrný počet návštěvnosti'),
        ),
    ]
