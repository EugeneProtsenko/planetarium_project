from django.db import transaction
from pip._vendor.rich.markup import Tag
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from planetarium.models import ShowTheme, PlanetariumDome, AstronomyShow


class ShowThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTheme
        fields = ("id", "name")


class PlanetariumDomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlanetariumDome
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class AstronomyShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_themes")


class AstronomyShowListSerializer(serializers.ModelSerializer):
    show_themes = serializers.SlugRelatedField(many=True,
                                               slug_field="name",
                                               read_only=True)

    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "show_themes")

