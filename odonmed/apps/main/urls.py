from django.conf.urls import patterns, url


urlpatterns = patterns('odonmed.apps.main.views',
                       url(r'^$', 'login_view', name="url_login"),
                       url(r'^logout/$', 'logout_view', name="url_logout"),
                       url(r'^perfil/(?P<username>\w+)/$', 'get_paciente', name="get_paciente"),
                       url(r'^perfil/(?P<username>\w+)/reserva/$', 'reserva_hora', name="reserva_hora"),
                       url(r'^buscar/$', 'busqueda_hora', name="busqueda_hora"),
                       url(r'^buscar/hora/$', 'get_hora', name="get_hora"),
                       url(r'^buscar/doctor/$', 'get_doctor', name="get_doctor"),
                       url(r'^registrar', 'registrar_view', name="url_registrar"),
                       url(r'^listado/$', 'get_disponible', name="url_disponibilidad"),
                       url(r'^listado/validar/$', 'get_validar', name="url_validar"),
                       url(r'^guardareserva/$', 'set_guardareserva', name="url_guardareserva"),
                    )

