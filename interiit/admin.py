from django.contrib import admin
from interiit.models import Profile, Details

class DetailsAdmin(admin.ModelAdmin):
	list_display = ('pk', 'user', 'sport', 'college')
admin.site.register(Details, DetailsAdmin)

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name', 'phone_number', 'email_id', 'blood_group' , 'Roll_number' , 'event1', 'event2', 'event3', 'relay_event1', 'relay_event2','timestamp',)
admin.site.register(Profile, ProfileAdmin)
