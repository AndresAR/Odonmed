from django.db import models
from ..pacientes.models import Paciente
from ..medicos.models import Medico


class Consulta(models.Model):
    medico = models.ManyToManyField(Medico)
    paciente = models.ManyToManyField(Paciente)


class Anamnesis(models.Model):
    paciente = models.OneToOneField(Paciente)
    diabetes = models.BooleanField()
    hipertension = models.BooleanField()
    cancer = models.BooleanField()
    alergias = models.CharField(max_length=120)


class ExamenBucal(models.Model):
    paciente = models.ManyToManyField(Paciente)
    caries = models.BooleanField()
    estado_ginvival = models.CharField(max_length=50)
    anomalia_dento_maxilofacial = models.CharField(max_length=50)
    mucosa_de_mejilla = models.CharField(max_length=50)
    lengua = models.CharField(max_length=50)
    frenillo_lingual = models.CharField(max_length=50)
    frenillo_labial_medio_superior = models.CharField(max_length=50)
    frenillo_labial_inferior = models.CharField(max_length=50)

class Tratamiento(models.Model):
    paciente = models.ManyToManyField(Paciente)
    pieza = models.PositiveIntegerField()
    material = models.CharField(max_length=50)
    cara = models.CharField(max_length=50)
    endodoncia = models.CharField(max_length=50)
    protesis = models.CharField(max_length=50)
    exodoncia = models.CharField(max_length=50)
    destartraje = models.CharField(max_length=50)
    protesis_removible = models.CharField(max_length=50)
