from django.contrib import admin

from .models import Genre, Actor, Ticket, Performance, TheatreHall, Reservation, Play


class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row")


class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("plays", "theatre_hall", "show_time")
    list_filter = ("theatre_hall", "show_time")


class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "created_at",
    )


class TicketAdmin(admin.ModelAdmin):
    list_display = ("row", "seat", "performance", "reservation")


admin.site.register(Performance, PerformanceAdmin)
admin.site.register(TheatreHall, TheatreHallAdmin)
admin.site.register(Genre)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Play)
