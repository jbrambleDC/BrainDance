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
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    ##Incorporate Preferences

    def __str__(self):
        return self.first_name + " " + self.last_name

class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    activity_location = models.ManyToManyField(Location) ###maybe OneToManyField
    activity_type = models.CharField(max_length=200)  ##add choices
    acttivity_season = models.CharField() ##add choices
    activity_date = models.DateTimeField(default=null)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.activity_name

    def get_price(self):
        return self.price
