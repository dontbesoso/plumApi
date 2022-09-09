from django.shortcuts import render
from django.db.models.functions import Lower

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from plum.models import Logowania, Pracownicy
from plum.serializers import LogowaniaSerializer, PracownicySerializer

@csrf_exempt
def logowaniaApi(request):
    if request.method=='GET':
        
        try:
            useridParam = request.GET['userid']
        except:
            useridParam = None
            
        try: 
            typeParam =  request.GET['type']
        except:
            typeParam = None

        
        """
        try:
            thevariable
        except NameError:
            print("well, it WASN'T defined after all!")
        else:
            print("sure, it was defined.")
        """


        if ((useridParam is not None) and (typeParam is not None)):
            logowania = Logowania.objects.filter(userid=useridParam, type=typeParam).order_by(Lower('id').desc())[:1]
        elif ((useridParam is not None) and (typeParam is None)):
            print("Wywołano -- ostatnie --")
            logowania = Logowania.objects.filter(userid=useridParam).order_by('-id')[:1]
        else:
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

        try:
            useridParam = request.GET['cardId']
        except:
            useridParam = None
                  
        if useridParam is not None:
            pracownicy = Pracownicy.objects.filter(cardId=useridParam).order_by(Lower('id').desc())[:1]
        else:
            pracownicy = Pracownicy.objects.all()

        pracownicy_serializer=PracownicySerializer(pracownicy,many=True)
        return JsonResponse(pracownicy_serializer.data,safe=False)
