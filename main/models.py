from django.db import models

# models.py
from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    max_members = models.IntegerField()
    current_members = models.IntegerField()
    apply_link = models.URLField(max_length=200, default='https://travelatb.com/')
    def __str__(self):
        return self.name

    def percentage(self):
        return (self.current_members / self.max_members) * 100 if self.max_members > 0 else 0
