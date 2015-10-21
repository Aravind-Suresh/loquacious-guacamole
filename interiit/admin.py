from django.contrib import admin
from interiit.models import Profile, Details

class DetailsAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'sport', 'college')
admin.site.register(Details, DetailsAdmin)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name','gender','phone_number', 'email_id', 'blood_group' , 'Roll_number' , 'event','timestamp','participant_type','staff_type',)
admin.site.register(Profile, ProfileAdmin)


    
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