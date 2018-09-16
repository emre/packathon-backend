from django.contrib import admin
from common.models import Hacker
from django.contrib.auth.admin import UserAdmin


class HackerAdmin(UserAdmin):
    """
    Custom user in Django Admin
    """
    list_display = ('__str__', 'username', 'name', 'team',)
    readonly_fields = ['voted_for']
    list_filter = ('team',)
    fieldsets = (
        ('Account Info', {
            'fields': ('username', 'name', 'email', 'team', 'is_staff',)
        }),
        ('Extra Details', {
            'fields': ('description', 'website', 'git', 'twitter',)
        }),
        ('Password', {
            'fields': ('password',)
        }),
    )

admin.site.register(Hacker, HackerAdmin)
