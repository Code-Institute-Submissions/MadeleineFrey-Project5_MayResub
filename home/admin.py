from django.contrib import admin
from .models import Team, Location, Contact


# Register your models here.
class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'role',
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'address',
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
    )

admin.site.register(Team, TeamAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
