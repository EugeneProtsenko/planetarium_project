from django.db import transaction
from pip._vendor.rich.markup import Tag
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from planetarium.models import ShowTheme


class ShowThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTheme
        fields = ("id", "name")
