from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=300)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Athlete(models.Model):
        team = models.ForeignKey(Team, on_delete=models.CASCADE)
        name = models.CharField(max_length=250)
        weight = models.FloatField
