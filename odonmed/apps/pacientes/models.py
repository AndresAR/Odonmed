from django.db import models
from django.contrib.auth.models import User


class Paciente(models.Model):
    from choices import SEXO_CHOICES
    usuario = models.ForeignKey(User)
    direccion = models.CharField(max_length=50)
    telefono = models.PositiveIntegerField()
    sexo = models.CharField(max_length=50, choices=SEXO_CHOICES)
    fecha_de_nacimiento = models.DateField()

    def __unicode__(self):
        return u'%s %s' % (self.usuario.first_name, self.usuario.last_name)