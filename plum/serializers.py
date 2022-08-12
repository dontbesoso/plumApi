from rest_framework import serializers
#from EmployeeApp.models import Departments,Employees
from plum.models import Pracownicy, Logowania

"""
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments 
        fields=('DepartmentId','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees 
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')


"""

class LogowaniaSerializer(serializers.ModelSerializer): 
    class Meta:
        model=Logowania 
        fields=('id', 'userid', 'userName', 'timeIn', 'type', 'prevId', 'sessionId')
    
    

class PracownicySerializer(serializers.ModelSerializer):
    class Meta:
        model=Pracownicy 
        fields=('id', 'name', 'cardId', 'description', 'hasAdmin')
