from .models import Driver, Vehicle
from rest_framework import serializers


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class VehicleDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ("driver_id",)

