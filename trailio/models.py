from django.db import models
from django.utils import timezone
from datetime import *

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
    region_name = models.CharField(max_length=200, null=True, blank=True)
    lat = models.FloatField(blank=False, null=False)
    lon = models.FloatField(blank=False, null=False)
    weather = models.CharField(max_length=8, choices=WEATHER_CHOICES,default=MILD)

    def __str__(self):
        return self.loc_name

    def get_coords(self):
        return self.lat, self.lon

class User(models.Model):
    dt_str = "1/1/1900 12:00:00 PM"
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    birthdate = models.DateTimeField(null=False, blank=True, default=datetime.strptime(dt_str,"%m/%d/%Y %I:%M:%S %p"))
    email = models.EmailField()
    password = models.CharField(max_length=20,null=False, default='0')
    ##Incorporate Preferences

    def __str__(self):
        return self.first_name + " " + self.last_name

class Route(models.Model):
    user = models.ForeignKey(User)
    location = models.ManyToManyField(Location)
    created_at = models.DateTimeField(null=False, default=datetime.now())

class Itinerary(models.Model):
    user = models.ForeignKey(User)
    route = models.OneToOneField(Route)
    Activity = models.ManyToManyField(Activity)
    ##How to map Activity_to_location

class Preference(models.Model):
    user = models.ForeignKey(User)
    Activity = models.ForeignKey(Activity) ## ManyToManyField??
    rating = models.IntegerField(blank=True, null=True)
    Prefered = models.NullBooleanField()

class Infographic(models.Model):
    itinerary = models.OneToOneField(Itinerary)
    infographic_image = models.ImageField() ##  maybe should not store as image

class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    activity_location = models.ManyToManyField(Location) ###maybe OneToManyField
    activity_type = models.CharField(max_length=200)  ##add choices
    activity_weather = models.CharField(max_length=20, default='MILD') ##add choices
    begin_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    begin_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True) ##remember to validate begin_time < end_time
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
