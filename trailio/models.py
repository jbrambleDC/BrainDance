from django.db import models
from django.utils import timezone

class Location(models.Model):
    WARM = 'WARM'
    MILD = 'MILD'
    COLD = 'COLD'
    HOT = 'HOT'
    TROPICAL = 'TROPICAL'
    WEATHER_CHOICES = (
    (WARM, 'WARM'),
    (MILD, 'MILD'),
    (COLD, 'COLD'),
    (HOT, 'HOT'),
    (TROPICAL, 'TROPICAL'),
    )
    loc_name = models.CharField(max_length=200)
    country_name = models.CharField(max_length=200)
    lat = models.FloatField(blank=False, null=False)
    lon = models.FloatField(blank=False, null=False)
    weather = models.CharField(max_length=8, choices=WEATHER_CHOICES,default=MILD)

    def __str__(self):
        return self.loc_name

    def get_coords(self):
        return self.lat, self.lon

class User(models.Model):
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    birthdate = models.DateTimeField(null=False, blank=True, default='1900-01-01')
    email = models.EmailField()
    password = models.CharField(max_length=20,null=False, default='0')
    ##Incorporate Preferences

    def __str__(self):
        return self.first_name + " " + self.last_name

class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    activity_location = models.ManyToManyField(Location) ###maybe OneToManyField
    activity_type = models.CharField(max_length=200)  ##add choices
    activity_weather = models.CharField(max_length=20, default='MILD') ##add choices
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.activity_name

    def get_price(self):
        return self.price

    def get_duration(self):
        return self.end_date - self.begin_date ## will this work?

    def get_desc(self):
        return self.description
