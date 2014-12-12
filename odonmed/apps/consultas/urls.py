from django.conf.urls import patterns, url

urlpatterns = patterns('odonmed.apps.consultas.views',
                        url(r'^(\w+)/(\w+)$', 'inicio_view', name="inicio_view"),
                    )

