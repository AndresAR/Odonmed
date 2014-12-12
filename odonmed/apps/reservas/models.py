from django.db import models


class Reserva(models.Model):
    idMedico = models.IntegerField()
    idPaciente = models.IntegerField()
    idFecha = models.IntegerField()
    atendido = models.BooleanField()