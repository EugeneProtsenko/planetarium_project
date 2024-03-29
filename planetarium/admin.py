from django.contrib import admin

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    Reservation,
    ShowSession,
    Ticket,
)

admin.site.register(AstronomyShow)
admin.site.register(ShowTheme)
admin.site.register(PlanetariumDome)
admin.site.register(Reservation)
admin.site.register(ShowSession)
admin.site.register(Ticket)
