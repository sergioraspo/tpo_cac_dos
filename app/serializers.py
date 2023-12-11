from rest_framework import serializers
from app.models import Person
from app.models import Evento
from app.models import Opciones

class PersonSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Indico con que modelo se va a corresponder el serializador
        model = Person
        #listado defino los campos de la clase Movie que quiero serializar
        fields = ['first_name','last_name']

class EventoSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Indico con que modelo se va a corresponder el serializador
        model = Evento
        #listado defino los campos de la clase Movie que quiero serializar
        fields = ['Casamiento','Comunion', 'Fiesta de 15 años', 'Baby Shower', 'Corporativa']        

class OpcionesSerializer(serializers.ModelSerializer):
   
    class Meta:
        #Indico con que modelo se va a corresponder el serializador
        model = Opciones
        #listado defino los campos de la clase Movie que quiero serializar
        fields = ['Foto mural','Video con drone']