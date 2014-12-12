from django.contrib import admin
from models import Hora


class HoraAdmin(admin.ModelAdmin):
    class Meta:
        models = Hora

admin.site.register(Hora, HoraAdmin)
