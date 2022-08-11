from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from plum.models import Logowania, Pracownicy
from plum.serializers import LogowaniaSerializer, PracownicySerializer

@csrf_exempt
def logowaniaApi(request,id=0):
    if request.method=='GET':
        logowania = Logowania.objects.all()
        logowania_serializer=LogowaniaSerializer(logowania,many=True)
        return JsonResponse(logowania_serializer.data,safe=False)
    elif request.method=='POST':
        logowania=JSONParser().parse(request)
        logowania_serializer=LogowaniaSerializer(data=logowania)
        if logowania_serializer.is_valid():
            logowania_serializer.save()
            return JsonResponse("Pomyslnie dodano logowanie",safe=False)
        return JsonResponse("Nie udalo sie dodac rekordu",safe=False)

def pracownicyApi(request,id=0):
    if request.method=='GET':
        pracownicy = Pracownicy.objects.all()
        pracownicy_serializer=PracownicySerializer(pracownicy,many=True)
        return JsonResponse(pracownicy_serializer.data,safe=False)
