from django.shortcuts import render
from reservasAPP.models import *
from django.contrib.auth.decorators import login_required
from reservasAPP.forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def Dashboard(request):
    return render(request, 'modelApp/dashboard.html')

@login_required
def Estados(request):
    producto = Estado.objects.all()
    data = {
        'productos' : producto,
    }
    return render(request, 'modelApp/estados.html', data)

@login_required
def Reservas(request):
    reserva = Reserva.objects.all()
    data = {
        'reservas' : reserva,
    }
    return render(request, 'modelApp/reservas.html', data)

@login_required
def insertReserva(request):
    if request.method == 'POST':
        form = ReservasFormRegistration(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('reservas'))

    else:
        form = ReservasFormRegistration()

    data = {
        'form': form,
        'title': 'Insertar Reserva'
    }

    return render(request, 'modelApp/insertValues.html', data)

@login_required
def editarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    form = ReservasFormRegistration(instance=reserva)
    if request.method == 'POST':
        form = ReservasFormRegistration(request.POST, instance=reserva)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('reservas'))
        else:
            print("Hay errores: ", form.errors)
    data = {
        'form': form,
        'title': 'Editar Reserva'
    }
    return render(request, 'modelApp/insertValues.html', data)

@login_required
def dropReserva(request, id):
    if request.user.is_superuser:
        reserva = Reserva.objects.get(id = id)
        reserva.delete()
        return HttpResponseRedirect(reverse('reservas'))
    else:
        return render(request, 'modelApp/dashboard.html')