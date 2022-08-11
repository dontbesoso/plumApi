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
    
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        user = self.request.query_params.get('userid')
        if user is not None:
            queryset = Pracownicy.objects.get(userid__exact=user)
            #queryset = queryset.filter()
        return queryset
    
    class Meta:
        model=Logowania 
        fields=('id', 'userid', 'userName', 'timeIn', 'type', 'prevId', 'sessionId')
    
    

class PracownicySerializer(serializers.ModelSerializer):

    

    class Meta:
        model=Pracownicy 
        fields=('id', 'name', 'cardId', 'description', 'hasAdmin')
