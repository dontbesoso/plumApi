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
    userid = models.CharField(max_length=10)
    userName = models.CharField(max_length=64)
    timeIn = models.CharField(max_length=19)
    type = models.CharField(max_length=16)
    prevId = models.IntegerField()
    sessionId = models.IntegerField()
    machineName = models.CharField(max_length=64, default="")
    
class Pracownicy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    cardId = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    hasAdmin = models.BooleanField()
    password = models.CharField(max_length=64)
    passdate = models.CharField(max_length=10)
