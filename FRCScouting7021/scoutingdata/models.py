from django.db import models

# Create your models here.

class ScoutData():
    timestamp = models.DateTimeField()
    event = models.CharField()
    matchNumber = models.IntegerField()
    teamNumber = models.IntegerField()
    startingPosition = models.CharField()
    autoCrossedLine = models.BooleanField()
    autoSwitch = models.IntegerField()
    autoScale = models.IntegerField()
    teleSwitch = models.IntegerField()
    teleScale = models.IntegerField()
    teleExchange = models.IntegerField()
    endgameStatus = models.CharField()
    strategyNotes = models.TextField()
    otherNotes = models.TextField()

class Team():
    teamNum = models.IntegerField()