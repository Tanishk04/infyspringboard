
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserInfo1(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField(default='default@example.com')
    address = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=15)  # Use CharField for phone numbers
    password = models.CharField(max_length=128,default='')  # Add password field
    # confirm_password = models.CharField(max_length=128, default="")

    def __str__(self):
        return self.name

class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date_time = models.DateTimeField()
    venue = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.event_name

class Admin(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Booking(models.Model):
    user_name = models.CharField(max_length=200,default='')
    EVENT_CHOICES = [
        ('Birthday', 'Birthday'),
        ('Marriage', 'Marriage'),
        ('Conference', 'Conference'),
        ('New Product Launch', 'New Product Launch'),
        ('Musical Event for New Year', 'Musical Event for New Year'),
    ]
    event = models.CharField(max_length=100, choices=EVENT_CHOICES)
    booking_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200,default='')

    def __str__(self):
        return f'Booking {self.id} for {self.event} by {self.user_name}'
class Hall(models.Model):
    hall_name = models.CharField(max_length=50)
    capacity = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.hall_name


class Notification(models.Model):
    notificationId = models.IntegerField()
    userId = models.IntegerField()
    msg = models.CharField(max_length=200)
    sendTime = models.DateTimeField(default=timezone.now)  # Providing a default value here

    def __str__(self):
        return f'Notification {self.notificationId} sent at {self.sendTime}'
