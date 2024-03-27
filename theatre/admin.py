from django.contrib import admin

from .models import (
    Genre,
    Actor,
    Ticket,
    Performance,
    TheatreHall,
    Reservation,
    Play
)

admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Ticket)
admin.site.register(Performance)
admin.site.register(TheatreHall)
admin.site.register(Reservation)
admin.site.register(Play)
