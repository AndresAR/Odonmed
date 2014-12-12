from django.db import models
from django.contrib.auth.models import User
from ..horas.models import Hora


class Medico(models.Model):
    user = models.ForeignKey(User, unique=True)
    especialidad = models.CharField(max_length=50)
    dias = models.ManyToManyField(Hora)

    def __unicode__(self):
        return self.user.first_name
