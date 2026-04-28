from django.contrib import admin
from profiles.models import Profile, Follow

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "birth_date"]

@admin.register(Follow)
class Follow(admin.ModelAdmin):
    list_display = ["follower", "following", "created_at"]