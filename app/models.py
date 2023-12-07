from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone= models.IntegerField()
    
class Evento(models.Model):
    tipo= models.TextChoices("Casamiento", "Fiesta de 15 años")
    fecha_evento= models.DateField(auto_now=False, auto_now_add=False)
    horario=models.TextChoices("Diurno", "Nocturno")

class Opciones(models.Model):
    tipo= models.TextChoices("Foto mural", "Video con drone")

def __str__(self):
    return self.first_name
    return self.last_name
    return self.phone
    