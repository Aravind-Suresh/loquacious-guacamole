from django.contrib import admin
from interiit.models import Profile, Details

class DetailsAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'sport', 'college')
admin.site.register(Details, DetailsAdmin)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name','gender','phone_number', 'email_id', 'blood_group' , 'Roll_number' , 'event','timestamp','participant_type','staff_type',)
admin.site.register(Profile, ProfileAdmin)


