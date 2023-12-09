from django.shortcuts import render
from django.http import HttpResponse

#importo el modelo de movie
from app.models import Person
# from app.models import Evento
# from app.models import Opciones

#se importa el serializador creado
from app import serializers

#Se importan funcionalides del la libreria rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return HttpResponse('<h1>Hola Estudio Esplendor 📷</h1>')

@api_view(['GET']) #solo pueda ser accecido si la petición es GET
def inicio_app(request):
    Persona = Person.objects.all()
    serializer = serializers.PersonSerializer(Person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_person(request):
    serializer = serializers.PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Persona registrada correctamente',
                    'data':serializer.data}
        return Response(data= response, status=status.HTTP_201_CREATED)
    response = {'status':'Error',
                'message':'Persona no registrada',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_person(request):
    try:
        person = Person.objects.get()        
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Persona no identificada')

    serializer = serializers.PersonSerializer(person)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_person(request):
    try:
        person = Person.objects.get()        
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Persona no identificada')
    person.delete()
    return Response({'message':'registro eliminado'},status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_person(request):
    try:
        movie = Person.objects.get()
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Persona no identificada')
    serializer = serializers.PersonSerializer(Person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'Ok',
                    'message':'Persona registrada correctamente',
                    'data':serializer.data}
        return Response(data=response)
    response = {'status':'Error',
                'message':'Persona no registrada',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

