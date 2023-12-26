from dataclasses import fields
from django import forms
from django.urls import include
from reservasAPP.models import *
from django.core.validators import *

class ReservasFormRegistration(forms.Form):
    nombre = forms.CharField(max_length=255, required=True)
    telefono = forms.CharField(max_length=9, required=True)
    fecha_reserva = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    hora_reserva = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    cantidad_personas = forms.IntegerField(
        required=True, 
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15),
        ],
    )
    observacion = forms.CharField(max_length=255, required=False)
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), required=True)
    
    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fecha_reserva.widget.attrs['class'] = 'form-control'
    hora_reserva.widget.attrs['class'] = 'form-control'
    cantidad_personas.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    
class ReservasFormRegistration(forms.ModelForm):
    nombre = forms.CharField(max_length=255, required=True)
    telefono = forms.CharField(max_length=9, required=True)
    fecha_reserva = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    hora_reserva = forms.TimeField(required=True, widget=forms.TimeInput(attrs={'type': 'time'}))
    cantidad_personas = forms.IntegerField(
        required=True, 
        validators=[
            MinValueValidator(1),
            MaxValueValidator(15),
        ],
    )
    observacion = forms.CharField(max_length=255, required=False)
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), required=True)
    
    nombre.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    fecha_reserva.widget.attrs['class'] = 'form-control'
    hora_reserva.widget.attrs['class'] = 'form-control'
    cantidad_personas.widget.attrs['class'] = 'form-control'
    observacion.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Reserva
        fields = '__all__'
