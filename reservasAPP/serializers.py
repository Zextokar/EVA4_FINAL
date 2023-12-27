from rest_framework import serializers
from .models import Reserva, Estado

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['nombre']

class ReservaSerializer(serializers.ModelSerializer):
    estado_nombre = serializers.StringRelatedField(source='estado', read_only=True)

    class Meta:
        model = Reserva
        fields = ['id', 'nombre', 'telefono', 'fecha_reserva', 'hora_reserva', 'cantidad_personas', 'estado', 'estado_nombre', 'observacion']
