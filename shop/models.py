# shop/models.py
from django.db import models
from django.utils import timezone

class Trip(models.Model):
    STATUS_CHOICES = [
        ('current', 'Current'),
        ('past', 'Past'),
        ('future', 'Future'),
    ]

    name = models.CharField(max_length=200)
    ig_link = models.URLField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    max_places = models.PositiveIntegerField()
    taken_places = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='current')
    g_form = models.URLField(max_length=200, default="https://www.instagram.com/")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure taken_places is not greater than max_places
        if self.taken_places > self.max_places:
            self.taken_places = self.max_places
        super().save(*args, **kwargs)



class Option(models.Model):
    trip = models.ForeignKey(Trip, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price_increase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
