from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^panel/', include(admin.site.urls)),
                       url(r"^", include('odonmed.apps.main.urls')),
                       url(r"^medicos/", include('odonmed.apps.medicos.urls')),
                       url(r"^consultas/", include('odonmed.apps.consultas.urls')),
)
