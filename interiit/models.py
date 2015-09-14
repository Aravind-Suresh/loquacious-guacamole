from django.db import models
from django.contrib.auth.models import User
import os

FOOD_PREFERENCES = (
    ('veg', 'Vegetarian') , 
    ('nonveg', 'Non Vegetarian')
)

TSHIRT_TYPES = (
    ('s', 'S'), 
    ('m', 'M'), 
    ('l', 'L'), 
    ('xl', 'XL'), 
    ('xxl', 'XXL')
)

SPORTS_TYPES = (
    ('athletics', 'Athletics'),
    ('badminton', 'Badminton'),
    ('basketball', 'BasketBall'),
    ('cricket', 'Cricket'),
    ('football', 'Football'),
    ('hockey', 'Hockey'),
    ('squash', 'Squash'),
    ('swimming', 'Swimming'),
    ('tabletennis', 'TableTennis'),
    ('tennis', 'Tennis'),
    ('volleyball', 'VolleyBall'),
    ('waterpolo', 'WaterPolo'),
    ('weightlifting', 'Weightlifting')
)


SPORTS_EVENTS = (
    ('50 M Freestyle', '50 M Freestyle'),
    ('100 M Freestyle', '100 M Freestyle'),
    ('200 M Freestyle', '200 M Freestyle'),
    ('400 M Freestyle', '400 M Freestyle'), 
    ('1500 M Freestyle', '1500 M Freestyle'),
    ('50 M Breast Stroke', '50 M Breast Stroke'),
    ('100 M Breast Stroke', '100 M Breast Stroke'), 
    ('200 M Breast Stroke', '200 M Breast Stroke'), 
    ('50 M Back Stroke', '50 M Back Stroke'), 
    ('100 M Back stroke', '100 M Back stroke'), 
    ('200 M stroke', '200 M stroke'),
    ('50 M Butterfly', '50 M Butterfly'), 
    ('100 M Butterfly', '100 M Butterfly'), 
    ('200 M Individual Medley', '200 M Individual Medley')    
)

SPORTS_EVENTS_RELAY = (
    ('4x50 Freestyle Relay', '4x50 Freestyle Relay'),
    ('4x100 Freestyle Relay', '4x100 Freestyle Relay'), 
    ('4x100 Medley Relay', '4x100 Medley Relay')
)

GENDER_PREFERENCES = (
    ('M', 'Male'),
    ('F', 'Female')
)

class Details(models.Model):
    sport = models.CharField(max_length = 25, null = True, blank = True, choices = SPORTS_TYPES)
    user = models.ForeignKey(User,related_name='detail')
    college =  models.CharField(max_length = 25, null = True, blank = True)

    def __unicode__(self):
        return self.sport + self.college


def get_upload_path(self, filename):
    return os.path.join(str(self.user.detail.all()[0].college),str(self.user.detail.all()[0].sport), filename)

class Profile(models.Model):
    
    name = models.CharField(max_length = 25)
    #middle_name = models.CharField(max_length = 25, null = True, blank = True)
    #last_name = models.CharField(max_length = 25)
    
    gender = models.CharField(max_length = 1, choices = GENDER_PREFERENCES)
    #date_of_birth = models.DateTimeField()
    blood_group = models.CharField(max_length = 10)
    Roll_number = models.CharField(max_length= 15)
    event1 = models.CharField(max_length=35, null = True, blank = True, choices = SPORTS_EVENTS)
    event2 = models.CharField(max_length=35, null = True, blank = True, choices = SPORTS_EVENTS)
    event3 = models.CharField(max_length=35, null = True, blank = True, choices = SPORTS_EVENTS)
    relay_event1 = models.CharField(max_length=35, null = True, blank = True, choices = SPORTS_EVENTS_RELAY)
    relay_event2 = models.CharField(max_length=35, null = True, blank = True, choices = SPORTS_EVENTS_RELAY)
    phone_number = models.CharField(max_length = 10)
    parents_phone_number = models.CharField(max_length = 10)
    email_id = models.CharField(max_length = 100)
    image = models.ImageField(blank = True, null = True, upload_to = get_upload_path)
    food_preference = models.CharField(max_length = 20, choices = FOOD_PREFERENCES)
    
    tshirt_size = models.CharField(max_length = 5, choices = TSHIRT_TYPES)
    
    timestamp = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

