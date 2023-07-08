from rest_framework import serializers

from app.models import *
class CarsMS(serializers.ModelSerializer):
    class Meta:
        model=Cars
        fields="__all__"