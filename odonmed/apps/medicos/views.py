from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.models import User
from forms import LoginForm
from ..medicos.models import Medico
from ..pacientes.models import Paciente
from ..reservas.models import Reserva
from ..horas.models import Hora


def index_view(request):
    return render_to_response('medicos/login.html', context_instance=RequestContext(request))


def login_view(request):
    username = ""
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            if Medico.objects.filter(user__username=username):
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, "Te has identificado de modo correcto")
                    else:
                        messages.error(request, "Tu usuario esta innactivo")
            else:
                    messages.error(request, "El usuario no es medico")
        else:
            messages.error(request, "Nombre de usuario y/o password incorrecto")
    else:
        form = LoginForm()

    return render_to_response('medicos/perfil.html', locals(), context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('medicos/')


def get_paciente(request, med):
    m = med
    medico = Medico.objects.get(user=m)
    paciente = Paciente.objects.all()
    reserva = Reserva.objects.filter(idMedico=m)
    hora = Hora.objects.all()

    return render_to_response('medicos/perfil.html', locals(), context_instance=RequestContext(request))


def eliminar(request, paciente):
    paciente = paciente
    print paciente
