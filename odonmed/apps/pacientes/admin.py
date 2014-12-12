from django.contrib import admin
from models import Paciente


class PacienteAdmin(admin.ModelAdmin):
    class Meta:
        model = Paciente

admin.site.register(Paciente, PacienteAdmin)

