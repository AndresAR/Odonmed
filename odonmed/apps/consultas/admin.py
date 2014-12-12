from django.contrib import admin
from models import Consulta, Anamnesis, ExamenBucal, Tratamiento


class ConsultaAdmin(admin.ModelAdmin):
        model = Consulta


class AnamnesisAdmin(admin.ModelAdmin):
    class Meta:
        model = Anamnesis


class ExamenBucalAdmin(admin.ModelAdmin):
    class Meta:
        model = ExamenBucal


class TratamientoAdmin(admin.ModelAdmin):
    class Meta:
        model = Tratamiento


admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Anamnesis, AnamnesisAdmin)
admin.site.register(ExamenBucal, ExamenBucalAdmin)
admin.site.register(Tratamiento, TratamientoAdmin)

