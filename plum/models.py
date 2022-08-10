from django.db import models

# Create your models here.
"""
class Logowania(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Pracownicy(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

"""

class Logowania(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    userName = models.CharField(max_length=64)
    timeIn = models.CharField(max_length=19)
    type = models.CharField(max_length=16)
    prevId = models.IntegerField()
    sessionId = models.IntegerField()
    
class Pracownicy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    cardId = models.IntegerField()
    description = models.CharField(max_length=255)
    hasAdmin = models.BooleanField()
