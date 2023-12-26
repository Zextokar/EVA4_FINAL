from django.shortcuts import render
from reservasAPP.models import *
from django.contrib.auth.decorators import login_required
from reservasAPP.forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse

#Librerías necesarias API
from .serializers import ReservaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

# Views para el panel de control principal (Dashboard)
@login_required
def Dashboard(request):
    return render(request, 'modelApp/dashboard.html')

def APIinHTML(request):
    return render(request, 'modelApp/viewAPI.html')


# Views para mostrar los estados de productos
@login_required
def Estados(request):
    producto = Estado.objects.all()
    data = {
        'productos': producto,
    }
    return render(request, 'modelApp/estados.html', data)


# Views para mostrar las reservas existentes
@login_required
def Reservas(request):
    reserva = Reserva.objects.all()
    data = {
        'reservas': reserva,
    }
    return render(request, 'modelApp/reservas.html', data)


# Views para insertar nuevas reservas
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


# Views para editar reservas existentes
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


# Views para eliminar reservas existentes
@login_required
def dropReserva(request, id):
    if request.user.is_superuser:
        reserva = Reserva.objects.get(id=id)
        reserva.delete()
        return HttpResponseRedirect(reverse('reservas'))
    else:
        return render(request, 'modelApp/dashboard.html')
    
# Vista mediante API
@api_view(['GET'])
def vistaReservaAPI(request):
    reservas = Reserva.objects.all().order_by('fecha_reserva')
    reserva_list = ReservaSerializer(reservas, many=True).data
    data = {'reserva': reserva_list}
    return JsonResponse(data)

@api_view(['GET', 'POST'])
def vistaReservaApi2(request):
    if request.method == 'GET':
        reservas = Reserva.objects.all().order_by('fecha_reserva')
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReservaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    reserva = Reserva.objects.filter(id=pk).first()

    if not reserva:
        return Response({'error': 'Reserva no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ReservaSerializer(reserva)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservaSerializer(reserva, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reserva.delete()
        return Response({'message': 'Reserva eliminada correctamente'}, status=status.HTTP_204_NO_CONTENT)