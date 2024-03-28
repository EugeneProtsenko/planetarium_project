from django.shortcuts import render
from pip._vendor.rich.theme import Theme
from rest_framework import viewsets

from planetarium.models import ShowTheme, PlanetariumDome, AstronomyShow
from planetarium.serializers import ShowThemeSerializer, PlanetariumDomeSerializer, AstronomyShowSerializer


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
