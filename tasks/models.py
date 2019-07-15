from django.db import models

from users.models import EmailUser


class Task(models.Model):
    user = models.ForeignKey(EmailUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    text = models.CharField(max_length=3000)
    formula = models.CharField(max_length=255)

class Variable(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=6)
    value = models.FloatField()
