from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class MovieCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.name


class Movie(models.Model):
    class Status(models.TextChoices):
        DRAFT = ("dr", "عدم انتشار")
        PUBLISH = ("pu", "انتشار")

    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    director = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    actorList = models.TextField()
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    aboutMovie = models.TextField(null=True, blank=True)
    status = models.CharField(choices=Status.choices, max_length=2)

    def __str__(self):
        return self.name
