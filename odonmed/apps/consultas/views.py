from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, redirect
from ..medicos.models import Medico
from ..pacientes.models import Paciente
from ..consultas.models import Consulta, Anamnesis, ExamenBucal, Tratamiento
from forms import AnamnesisForm


def inicio_view(request, paciente, medico):
    paciente = Paciente.objects.get(usuario=paciente)
    anamnesis = Anamnesis.objects.filter(paciente_id=paciente)
    if Anamnesis.objects.filter(paciente_id=paciente):
        anamnesis = Anamnesis.objects.filter(paciente_id=paciente)
        return render_to_response('consultas/inicio.html', locals(), context_instance=RequestContext(request))
    else:
        if request.method == 'POST':
            anamnesisForm = AnamnesisForm(request.POST or None)
            if anamnesisForm.is_valid():
                paciente = paciente
                if 'diabetes' in request.POST:
                    diabetes = request.POST['diabetes']
                else:
                    diabetes = False

                if 'hipertension' in request.POST:
                    hipertension = request.POST['hipertension']
                else:
                    hipertension = False
                if 'cancer' in request.POST:
                    cancer = request.POST['cancer', False]
                else:
                    cancer = False
                alergias = request.POST['alergias']


                anamnesis.paciente = paciente
                anamnesis.diabetes = diabetes
                anamnesis.hipertension = hipertension
                anamnesis.cancer = cancer
                anamnesis.alergias = alergias
                anamnesis.save()

                return render_to_response('consultas/inicio.html', locals(), context_instance=RequestContext(request))
        else:
            anamnesisForm = AnamnesisForm()
        data = {
            'anamnesisForm': anamnesisForm
        }
        return render_to_response('consultas/inicio.html', locals(), context_instance=RequestContext(request))
