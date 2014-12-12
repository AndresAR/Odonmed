from django.contrib import admin
from models import Reserva


class ReservaAdmin(admin.ModelAdmin):
    class Meta:
        model = Reserva

admin.site.register(Reserva, ReservaAdmin)

