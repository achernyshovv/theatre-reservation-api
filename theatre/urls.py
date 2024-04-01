from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GenreViewSet,
    ActorViewSet,
    PlayViewSet,
    TheatreHallViewSet,
    PerformanceViewSet,
    ReservationViewSet,
    TicketViewSet,
)


router = DefaultRouter()


router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"plays", PlayViewSet)
router.register(r"theatrehalls", TheatreHallViewSet)
router.register(r"performances", PerformanceViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"tickets", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]


app_name = "theatre"
