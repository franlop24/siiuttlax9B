from django.db import models

# Create your models here.

class Career(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)
    director = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    plan = models.CharField(max_length=4)
    status = models.BooleanField()

class Subject(models.Model):
    name = models.CharField(max_length=50)
    semester = models.IntegerField()
    total_hours = models.IntegerField()
    hours_semesters = models.IntegerField()
    file = models.CharField(max_length=50)



