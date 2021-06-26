from django.db import models
from django.db.models.fields import CharField


# Create your models here.

class Calc(models.Model):
    num1 = CharField(max_length=64)
    num2 = CharField(max_length=64)
    oper = CharField(max_length=64)
    result = CharField(max_length=64)


class Quest(models.Model):
    quest = CharField(max_length=256)
    correct = CharField(max_length=64)
    wrong1 = CharField(max_length=64)
    wrong2 = CharField(max_length=64)
    wrong3 = CharField(max_length=64)