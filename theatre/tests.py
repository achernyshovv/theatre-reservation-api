from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket

from django.utils import timezone

from .serializers import (
    GenreSerializer,
    ActorSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    TicketSerializer,
)


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="12345",
        )
        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.play = Play.objects.create(
            title="Test Play", description="Test description"
        )
        self.play.genres.add(self.genre)
        self.play.actors.add(self.actor)
        self.theatre_hall = TheatreHall.objects.create(
            name="Test Hall", rows=10, seats_in_row=20
        )
        self.performance = Performance.objects.create(
            plays=self.play, theatre_hall=self.theatre_hall, show_time=timezone.now()
        )
        self.reservation = Reservation.objects.create(user=self.user)

    def test_genre_creation(self):
        self.assertEqual(self.genre.name, "Drama")

    def test_actor_creation(self):
        self.assertEqual(self.actor.full_name, "John Doe")

    def test_play_creation(self):
        self.assertEqual(self.play.title, "Test Play")
        self.assertEqual(self.play.description, "Test description")
        self.assertEqual(self.play.genres.count(), 1)
        self.assertEqual(self.play.actors.count(), 1)

    def test_theatre_hall_creation(self):
        self.assertEqual(self.theatre_hall.name, "Test Hall")
        self.assertEqual(self.theatre_hall.rows, 10)
        self.assertEqual(self.theatre_hall.seats_in_row, 20)

    def test_performance_creation(self):
        self.assertEqual(self.performance.plays.title, "Test Play")
        self.assertEqual(self.performance.theatre_hall.name, "Test Hall")

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.user.email, "test@example.com")

    def test_ticket_creation(self):
        ticket = Ticket.objects.create(
            row=1, seat=1, performance=self.performance, reservation=self.reservation
        )
        self.assertEqual(ticket.row, 1)
        self.assertEqual(ticket.seat, 1)
        self.assertEqual(ticket.performance.plays.title, "Test Play")
        self.assertEqual(ticket.reservation.user.email, "test@example.com")

    def test_str_methods(self):
        self.assertEqual(str(self.genre), "Drama")
        self.assertEqual(str(self.actor), "John - Doe")
        self.assertEqual(str(self.play), "Test Play")
        self.assertEqual(str(self.theatre_hall), "Test Hall")
        self.assertEqual(str(self.performance), "Test Play")
        self.assertIn("test@example.com", str(self.reservation))


class SerializerTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="12345",
        )
        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.play = Play.objects.create(
            title="Test Play", description="Test description"
        )
        self.play.genres.add(self.genre)
        self.play.actors.add(self.actor)
        self.theatre_hall = TheatreHall.objects.create(
            name="Test Hall", rows=10, seats_in_row=20
        )
        self.performance = Performance.objects.create(
            plays=self.play, theatre_hall=self.theatre_hall, show_time=timezone.now()
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.ticket = Ticket.objects.create(
            row=1, seat=1, performance=self.performance, reservation=self.reservation
        )

    def test_genre_serializer(self):
        serializer = GenreSerializer(instance=self.genre)
        self.assertEqual(serializer.data["name"], "Drama")

    def test_actor_serializer(self):
        serializer = ActorSerializer(instance=self.actor)
        self.assertEqual(serializer.data["first_name"], "John")
        self.assertEqual(serializer.data["last_name"], "Doe")

    def test_play_serializer(self):
        serializer = PlaySerializer(instance=self.play)
        self.assertEqual(serializer.data["title"], "Test Play")
        self.assertEqual(serializer.data["description"], "Test description")
        self.assertEqual(serializer.data["genres"][0]["name"], "Drama")
        self.assertEqual(serializer.data["actors"][0]["first_name"], "John")
        self.assertEqual(serializer.data["actors"][0]["last_name"], "Doe")

    def test_theatre_hall_serializer(self):
        serializer = TheatreHallSerializer(instance=self.theatre_hall)
        self.assertEqual(serializer.data["name"], "Test Hall")
        self.assertEqual(serializer.data["rows"], 10)
        self.assertEqual(serializer.data["seats_in_row"], 20)

    def test_performance_serializer(self):
        serializer = PerformanceSerializer(instance=self.performance)
        self.assertEqual(serializer.data["plays"], self.play.id)
        self.assertEqual(serializer.data["theatre_hall"]["name"], "Test Hall")

    def test_reservation_serializer(self):
        serializer = ReservationSerializer(instance=self.reservation)
        self.assertEqual(serializer.data["user"], self.user.id)

    def test_ticket_serializer(self):
        serializer = TicketSerializer(instance=self.ticket)
        self.assertEqual(serializer.data["row"], 1)
        self.assertEqual(serializer.data["seat"], 1)
        self.assertEqual(serializer.data["performance"]["id"], self.performance.id)
        self.assertEqual(serializer.data["reservation"]["user"], self.user.id)
