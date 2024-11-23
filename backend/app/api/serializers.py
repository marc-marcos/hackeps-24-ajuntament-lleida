from rest_framework import serializers

from .models import Parking, Planta, Plaza, PlazaLog


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking

        fields = "__all__"


class PlantaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planta

        fields = "__all__"


class PlazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plaza

        fields = "__all__"


class PlazaLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlazaLog

        fields = "__all__"
