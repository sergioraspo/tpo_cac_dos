from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Evento(models.Model):
    CASAMIENTO = 'CM'
    COMUNION = 'CO'
    FIESTA_15 = 'F15'
    BABY_SHOWER = 'BS'
    CORPORATIVA = 'CP'
    TIPOS_DE_EVENTO = [
        (CASAMIENTO, 'Casamiento'),
        (COMUNION, 'Comunión'),
        (FIESTA_15, 'Fiesta de 15 años'),
        (BABY_SHOWER, 'Baby Shower'),
        (CORPORATIVA, 'Corporativa'),
    ]
    tipo_de_evento = models.CharField(
        max_length=3,
        choices=TIPOS_DE_EVENTO,
        default=CASAMIENTO,
    )

    def evento(self):
        return self.tipo_de_evento in {self.CASAMIENTO, self.CORPORATIVA}    

class Opciones(models.Model):
    TIPO_CHOICES = [
        ('F', 'Foto mural'),
        ('V', 'Video con drone'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)

    def __str__(self):
        return self.tipo
