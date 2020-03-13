from rest_framework import serializers
from .models import Light


class LightModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Light
        fields = "__all__"