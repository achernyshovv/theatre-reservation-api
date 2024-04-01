from rest_framework.response import Response
from rest_framework import viewsets, status
from theatre.permissions import IsAdminOrIfAuthenticatedReadOnly
from .models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket
from drf_spectacular.utils import extend_schema

from .serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    TicketSerializer,
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of genres")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific genre")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new genre")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update a genre")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of a genre")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete a genre")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of actors")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific actor")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new actor")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update an actor")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of an actor")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete an actor")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of plays")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific play")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new play")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update a play")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of a play")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete a play")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of theatre halls")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific theatre hall")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new theatre hall")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update a theatre hall")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of a theatre hall")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete a theatre hall")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of performances")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific performance")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new performance")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update a performance")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of a performance")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete a performance")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of reservations")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific reservation")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new reservation")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update a reservation")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of a reservation")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete a reservation")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    @extend_schema(summary="Retrieve a list of tickets")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(summary="Retrieve a specific ticket")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="Create a new ticket")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="Update a ticket")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="Partial update of a ticket")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="Delete a ticket")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        performance_id = serializer.validated_data.get("performance")
        seat_row = serializer.validated_data.get("row")
        seat_number = serializer.validated_data.get("seat")

        try:
            performance = Performance.objects.get(id=performance_id)
        except Performance.DoesNotExist:
            return Response(
                {"message": "Performance not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if performance.available_seats <= 0:
            return Response(
                {"message": "No available seats for this performance"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if Ticket.objects.filter(
            performance=performance, row=seat_row, seat=seat_number
        ).exists():
            return Response(
                {"message": "Seat already reserved"}, status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)

        performance.available_seats -= 1
        performance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
