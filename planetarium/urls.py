from django.urls import path, include
from rest_framework import routers

from planetarium.views import ShowThemeViewSet, PlanetariumDomeViewSet, AstronomyShowViewSet, ShowSessionViewSet

router = routers.DefaultRouter()

router.register("show-themes", ShowThemeViewSet)
router.register("planetarium-dome", PlanetariumDomeViewSet)
router.register("astronomy-show", AstronomyShowViewSet)
router.register("show-session", ShowSessionViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "planetarium"
