from django.shortcuts import render
from api import serializers
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from .serializers import LightModelSerializer
from .models import Light
# Create your views here.

class LampListAPIView(ListAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer


class LampCreateAPIView(CreateAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer

class LampUpdateAPIView(UpdateAPIView):
    queryset = Light.objects.all()
    serializer_class = LightModelSerializer
