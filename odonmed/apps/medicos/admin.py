from django.contrib import admin
from models import Medico


class MedicoAdmin(admin.ModelAdmin):
    class Meta:
        model = Medico

admin.site.register(Medico, MedicoAdmin)
