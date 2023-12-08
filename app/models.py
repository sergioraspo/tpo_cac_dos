from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Evento(models.Model):
    TIPO_CHOICES = [
        ('C', 'Casamiento'),
        ('O', 'Corporativas'),
    ]
    HORARIO_CHOICES = [
        ('V', 'Vespertino'),
        ('N', 'Nocturno'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    fecha_evento = models.DateField(auto_now=False, auto_now_add=False)
    horario = models.CharField(max_length=1, choices=HORARIO_CHOICES)

    def __str__(self):
        return f"{self.tipo} - {self.fecha_evento} - {self.horario}" 


class Opciones(models.Model):
    TIPO_CHOICES = [
        ('F', 'Foto mural'),
        ('V', 'Video con drone'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

    def __str__(self):
        return self.tipo
