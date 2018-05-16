from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(max_length = 150, upload_to='uploads/%Y/%M/%D')
    image_description = models.CharField(max_length=40)
    num_people = models.IntegerField(default=0)

    def __str__(self):
            return self.name

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    trips_total = models.IntegerField(default=0)
    trips = models.ManyToManyField(Trip)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
