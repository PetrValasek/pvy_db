from django.core.validators import validate_email
from django.db import models
######################################################################################################
######################################################################################################


class Sponsors(models.Model):
    support_logo = models.ImageField(
        upload_to='Photo/Sponzori/',
        null=True,
        blank=True
    )

    support_id = models.CharField(
        max_length=50,
        null=True,
        verbose_name='Název', )

    support_text = models.TextField(
        max_length=400,
        verbose_name='Bližší specifikace firmy',
        null=True,
        blank=True, )

    class Meta:
        verbose_name = 'Sponzoři'
        verbose_name_plural = 'Sponzoři'
        ordering = ['-support_id']

    def __str__(self):
        return self.support_id


######################################################################################################
######################################################################################################


class Tournaments(models.Model):

    tournament_id = models.CharField(
        max_length=80,
        null=True,
        verbose_name='Turnaj',
        help_text='Název turnaje/akce/id')

    tournament_description = models.TextField(
        max_length=400,
        verbose_name='Turnaj',
        null=True,
        blank=True,
        help_text='Stručný popis turnaje')

    tournament_timeline = models.BooleanField(
        choices=[(True, 'Konalo se'), (False, 'Bude se konat')],
        default=True)

    tournament_mainfight = models.CharField(
        max_length=80,
        null=True,
        verbose_name='Hlavní zápas',
        help_text='Hlavní zápas + výherce')

    tournament_attendance = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='Největší návštěvnost organizace', )

    class Meta:
        verbose_name = 'Turnaj'
        verbose_name_plural = 'Turnaje'

    def __str__(self):
        return self.tournament_id

    ######################################################################################################
    ######################################################################################################


class Organisation(models.Model):

    organisation_logo = models.ImageField(
        upload_to='Photo/Organizace/',
        null=True,
        blank=True
    )

    organisation_name = models.CharField(
        max_length=100,
        null=True,
        verbose_name="Zadejte název společnosti"
    )

    organisation_short = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Zadejte zkratku společnosti"
    )

    organisation_year = models.PositiveIntegerField(
        default=2016,
        verbose_name='Rok',
        help_text='Zadejte rok založení společnosti')

    organisation_owner = models.CharField(
        max_length=80,
        null=True,
        verbose_name='Prezident/ředitel',)

    organisation_residence = models.CharField(
        max_length=80,
        null=True,
        verbose_name='Sídlo',
        help_text='Kde organizace sídlí - Země')

    organisation_highest = models.ForeignKey(
        Tournaments,
        null=True,
        blank=True,
        verbose_name='Největší turnaj',
        on_delete=models.CASCADE, )

    organisation_support = models.ForeignKey(
        Sponsors,
        null=True,
        blank=True,
        verbose_name='Největší sponzor',
        on_delete=models.CASCADE, )

    class Meta:
        verbose_name = 'Organizace'
        verbose_name_plural = 'Organizace'
        ordering = ['-organisation_name']

    def __str__(self):
        return f'{self.organisation_name} ,{str(self.organisation_short)}, {str(self.organisation_residence)}'


######################################################################################################
######################################################################################################


class Fighter(models.Model):

    Fighter_photo = models.ImageField(
        upload_to='Photo/Zapasnici/',
        null=True,
        blank=True
    )

    Fighter_id = models.CharField(
        max_length=60,
        null=True,
        verbose_name='Jméno a příjmení')

    Fighter_Country = models.CharField(
        max_length=60,
        null=True,
        verbose_name='Země',
        help_text='Země odkud zápasník pochází - kde byl narozen')

    Fighter_Height = models.PositiveIntegerField(
        default=180,
        blank=True,
        verbose_name='Výška zápasníka v cm')

    Fighter_Weight = models.FloatField(
        default=82.5,
        blank=True,
        max_length=3,
        verbose_name='Váha zápasníka v Kg')

    Fighter_description = models.PositiveIntegerField(
        default=20,
        verbose_name='Věk zápasníka')

    Fighter_email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        validators=[validate_email]
    )

    Fighter_score_Win = models.PositiveIntegerField(
        verbose_name='Počet výher',
        default=0,
        null=True,
        blank=True)

    Fighter_score_Losses = models.PositiveIntegerField(
        verbose_name='Počet proher',
        default=0,
        null=True,
        blank=True)

    Fighter_fighting_year = models.PositiveIntegerField(
        verbose_name='Celkové počet let',
        default=1,
        null=True,
        blank=True,
        help_text='Počet let, od započatí tréninku')

    Figher_networth = models.FloatField(
        verbose_name='Celkové jmění',
        help_text='Finanční kapitál v $',
        max_length=10,
        default=1000,
        null=True,
        blank=True,)

    Fighter_organisation = models.ForeignKey(
        Organisation,
        null=True,
        verbose_name='Organizace',
        on_delete=models.CASCADE,)

    class Meta:
        verbose_name = 'Zápasník'
        verbose_name_plural = 'Zápasníci'
        ordering = ['-Fighter_id']

    def __str__(self):
        return f'{self.Fighter_id} ({str(self.Fighter_score_Win)})'
