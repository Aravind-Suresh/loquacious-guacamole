from django.db import models
from django.contrib.auth.models import User
import os

FOOD_PREFERENCES = (
    ('veg', 'Vegetarian') , 
    ('nonveg', 'Non Vegetarian'),
    ('jain','jain')
)

TSHIRT_TYPES = (
    ('s', 'S'), 
    ('m', 'M'), 
    ('l', 'L'), 
    ('xl', 'XL'), 
    ('xxl', 'XXL'),
)

SPORTS_TYPES = (
    ('Staff','Staff'),
    ('Athletics', 'Athletics'),
    ('Badminton', 'Badminton'),
    ('Basketball', 'Basketball'),
    ('Cricket', 'Cricket'),
    ('Football', 'Football'),
    ('Hockey', 'Hockey'),
    ('Squash', 'Squash'),
    ('Table Tennis', 'Table Tennis'),
    ('Tennis', 'Tennis'),
    ('Volleyball', 'Volleyball'),
    ('Weightlifting', 'Weightlifting'),
)


SPORTS_EVENTS = (
    ('100 M', '100 M'),
    ('200 M', '200 M'),
    ('400 M', '400 M'),
    ('400 M', '400 M'), 
    ('800 M', '800 M'),
    ('1500 M', '1500 M'),
    ('5000 M', '5000 M'), 
    ('110 M Hurdles', '110 M Breast Stroke'), 
    ('400 M Hurdles', '400 M Hurdles'), 
    ('High Jump', 'High Jump'), 
    ('Long Jump', 'Long Jump'),
    ('Triple Jump', 'Triple Jump'), 
    ('Pole Vault', 'Pole Vault'), 
    ('Shot Put', 'Shot Put'),
    ('Discuss Throw', 'Discuss Throw'),    
    ('Javelin Throw', 'Javelin Throw'),    
    ('Hammer Throw', 'Hammer Throw'),    
    ('4x100 M Relay', '4x100 M Relay'),    
    ('4x400 M Relay', '4x400 M Relay'),    
)

STAFF_TYPE = (
    ('Coach','Coach'),
    ('Faculty','Faculty'),
    ('Sports Officer','Sports Officer'),
    ('Supporting Staff','Supporting Staff')
    )

GENDER_PREFERENCES = (
    ('M', 'Male'),
    ('F', 'Female')
)

BLOOD_GROUP_SEL = (
    ('O+ve','O+ve'),
    ('O-ve','O-ve'),
    ('A+ve','A+ve'),
    ('A-ve','A-ve'),
    ('B+ve','B+ve'),
    ('B-ve','B-ve'),
    ('AB+ve','AB+ve'),
    ('AB-ve','AB-ve'),

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
    
    name = models.CharField(max_length = 100, null = True, blank = True,)
    #middle_name = models.CharField(max_length = 25, null = True, blank = True)
    #last_name = models.CharField(max_length = 25)
    
    gender = models.CharField(max_length = 1, null = True, blank = True, choices = GENDER_PREFERENCES)
    #date_of_birth = models.DateTimeField()
    blood_group = models.CharField(max_length = 10, null = True, blank = True,choices = BLOOD_GROUP_SEL)
    Roll_number = models.CharField(max_length= 15, null = True, blank = True,)
    event = models.CharField(max_length=35, null = True, blank = True)
    participant_type = models.CharField(max_length=35, null = True, blank = True)
    staff_type = models.CharField(max_length=35, null = True, blank = True, choices = STAFF_TYPE)
    phone_number = models.CharField(max_length = 10, null = True, blank = True,)
    parents_phone_number = models.CharField(max_length = 10, null = True, blank = True,)
    email_id = models.CharField(max_length = 100)
    image = models.ImageField(blank = True, null = True, upload_to = get_upload_path)
    food_preference = models.CharField(max_length = 20, choices = FOOD_PREFERENCES)
    
    tshirt_size = models.CharField(max_length = 5, null = True, blank = True, choices = TSHIRT_TYPES)
    
    timestamp = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.event

