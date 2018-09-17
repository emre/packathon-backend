from django.contrib import admin
from common.models import Hacker
from django.contrib.auth.admin import UserAdmin


class HackerAdmin(UserAdmin):
    """
    Custom user in Django Admin
    """
    list_display = ('__str__', 'username', 'name',)
    fieldsets = (
        ('Account Info', {
            'fields': ('username', 'name', 'team', 'is_staff',)
        }),
        ('Extra Details', {
            'fields': ('profile_about', 'profile_location', 'profile_image',)
        }),
    )

admin.site.register(Hacker, HackerAdmin)
