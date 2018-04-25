from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Trip_model(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
