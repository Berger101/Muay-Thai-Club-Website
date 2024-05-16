from django.db import models
from django.contrib.auth.models import User


class TrainingSession(models.Model):
    instructor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
