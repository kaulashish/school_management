from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Class(models.Model):
    class_choices = [
        ("12th", "12th"),
        ("11th", "11th"),
        ("10th", "10th"),
        ("9th", "9th"),
        ("8th", "8th"),
    ]
    name = models.CharField(max_length=100, choices=class_choices)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    room_no = models.IntegerField(
        default=000,
        validators=[MaxValueValidator(999), MinValueValidator(000)],
        unique=True,
    )

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(
        default=0, validators=[MaxValueValidator(99), MinValueValidator(1)]
    )
    marks = models.IntegerField(
        default=0, validators=[MaxValueValidator(99), MinValueValidator(1)]
    )
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
    roll_no = models.IntegerField(
        default=0, validators=[MaxValueValidator(99), MinValueValidator(1)], unique=True
    )

    def __str__(self):
        return self.name
