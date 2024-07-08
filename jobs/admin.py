
from django.contrib import admin
from .models import CustomUser, Job, Application
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'surname', 'location', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Job)
admin.site.register(Application)
