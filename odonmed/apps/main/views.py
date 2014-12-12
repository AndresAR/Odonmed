from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import timezone
from forms import SignUpForm, LoginForm
from ..pacientes.models import Paciente
from ..medicos.models import Medico
from ..horas.models import Hora
from ..reservas.models import Reserva
import datetime
from django.core import serializers
from django.http import HttpResponse, Http404


def index_view(request):
    return render_to_response('main/login.html', context_instance=RequestContext(request))


def registrar_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            paciente = Paciente(usuario_id=user.id,telefono=1111111,fecha_de_nacimiento='1111-01-01')
            paciente.save()
            return redirect('/')
    else:
        form = SignUpForm()
    data = {
        'form': form,
    }
    return render_to_response('main/registrar.html', data, context_instance=RequestContext(request))


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Te has identificado de modo correcto")
                else:
                    messages.error(request, "Tu usuario esta innactivo")
            else:
                messages.error(request, "Nombre de usuario y/o password incorrecto")
    else:
        form = LoginForm()

    return render_to_response('main/perfil.html', locals(), context_instance=RequestContext(request))


def get_paciente(request, username):
    p = Paciente.objects.get(usuario__username=username)
    r = Reserva.objects.filter(idPaciente=p.id)

    ctx = {'pacientes': p, 'reserva': r}

    return render_to_response('main/perfil.html', ctx, context_instance=RequestContext(request))


def reserva_hora(request, username):
    m = Medico.objects.all()
    try:
        p = Paciente.objects.get(usuario__username=username)
    except Paciente.DoesNotExist:
        raise Http404

    ctx = {'pacientes': p, 'medicos': m}

    return render_to_response('main/reserva.html', ctx, context_instance=RequestContext(request))


def busqueda_hora(request):
    fecha = request.GET['hora']
    fin = timezone.now() + datetime.timedelta(days=20)
    hora = Hora.objects.filter(dias__range=[fecha, fin])
    ctx = serializers.serialize('json', hora)

    return HttpResponse(ctx, mimetype='application/json')


def get_hora(request):
    h = Hora.objects.filter(id=request.GET['hora'])
    ctx = serializers.serialize('json', h)

    return HttpResponse(ctx, mimetype='application/json')


def get_doctor(request):
    d = User.objects.filter(id=request.GET['doctor'])
    ctx = serializers.serialize('json', d)

    return HttpResponse(ctx, mimetype='application/json')


def get_disponible(request):
    medico = request.GET['medico']
    fecha = request.GET['fecha']
    idFecha = Hora.objects.filter(dias=fecha).values('id')
    valida = Medico.objects.filter(dias=idFecha, id=medico)
    if valida:
            horas = Hora.objects.filter(medico__id=medico, dias=fecha)
            ctx = serializers.serialize('json', horas)
            return HttpResponse(ctx, mimetype='application/json')
    else:
            horas = Hora.objects.filter(medico__id=medico, dias=fecha)
            ctx = serializers.serialize('json', horas)
            return HttpResponse(ctx, mimetype='application/json')


def get_validar(request):
    medico = request.GET['medico']
    fecha = request.GET['fecha']
    valida = Reserva.objects.filter(idMedico=medico, idFecha=fecha)
    ctx = serializers.serialize('json', valida)
    return HttpResponse(ctx, mimetype='application/json')


def set_guardareserva(request):
    medico = request.GET['medico']
    fecha = request.GET['fecha']
    paciente = request.GET['paciente']
    reserva = Reserva(idMedico=medico, idPaciente=paciente, idFecha=fecha, atendido=False)
    reserva.save()

    return render_to_response('main/perfil.html', locals(), context_instance=RequestContext(request))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')