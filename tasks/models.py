from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    text = models.CharField()
    formula = models.CharField(max_length=255)

class Variable(models.Model):
    solution = models.ForeignKey(Task, on_delete=models.CASCADE)
    name = models.CharField(max_length=5)
    value = models.FloatField()
