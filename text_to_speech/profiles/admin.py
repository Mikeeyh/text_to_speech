from django.contrib import admin
from django.contrib.auth import get_user_model

from text_to_speech.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'date_of_birth', 'gender', 'profile_picture', 'account_balance')

