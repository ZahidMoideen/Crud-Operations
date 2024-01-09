from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    amount = models.BigIntegerField()
    duration = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

class Login(models.Model):
    username = models.CharField(max_length=90)
    password = models.CharField(max_length=90)