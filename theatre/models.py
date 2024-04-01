from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Play(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        # genre_names = ', '.join(genre.name for genre in self.genres.all())
        # actor_names = ', '.join(actor.full_name for actor in self.actors.all())
        return f"{self.title}"


class TheatreHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Performance(models.Model):
    plays = models.ForeignKey(Play, on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.plays.title}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.created_at} {self.user}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"Ticket for "
            f"{self.performance.plays}"
            f" (Row: {self.row},"
            f" Seat: {self.seat}"
            f" by {self.reservation.user})"
        )
