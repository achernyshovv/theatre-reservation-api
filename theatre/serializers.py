from rest_framework import serializers
from django.contrib.auth import get_user_model

from user.serializers import UserSerializer
from .models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket

User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class PlaySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = "__all__"


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = "__all__"


class PerformanceSerializer(serializers.ModelSerializer):
    play = PlaySerializer(read_only=True)
    theatre_hall = TheatreHallSerializer()

    class Meta:
        model = Performance
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())

    class Meta:
        model = Reservation
        fields = ["id", "created_at", "user"]


class TicketSerializer(serializers.ModelSerializer):
    performance = PerformanceSerializer(read_only=True)
    reservation = ReservationSerializer(read_only=True)
    user = UserSerializer(source="reservation.user", read_only=True)
    play = PlaySerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"
