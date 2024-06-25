# models.py
import uuid

from django.db import models
from django.contrib.auth.models import User

class Brewery(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    website_url = models.URLField(max_length=200)
    # rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

class Review(models.Model):
    objects = None
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SCORE = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    scores = models.IntegerField(choices=SCORE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class BrewPub(models.Model):
    DoesNotExist = None
    objects = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    website_url = models.URLField()
    # rating = models.DecimalField(max_digits=3, decimal_places=2)

