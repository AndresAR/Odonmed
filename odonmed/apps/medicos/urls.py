from django.conf.urls import patterns, url

urlpatterns = patterns('odonmed.apps.medicos.views',
                        url(r'^$', 'login_view', name="login_view"),
                        url(r'^(\w+)/$', 'get_paciente', name="get_paciente"),
                        url(r'^eliminar/(\w+)/$', 'eliminar', name="eliminar"),
                    )

