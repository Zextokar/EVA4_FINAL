from django.db import models

# Create your models here.

class Estado(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.IntegerField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=255, blank=True)