from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date') # Defining table column names for 'Team' table
    list_display_links = ('id', 'thumbnail' , 'first_name',) # This makes id & first_name column clickable
    search_fields = ('first_name', 'last_name', 'designation') # We can search by this fields
    list_filter = ('designation',) # We get a filter option in the side on these fields
    
admin.site.register(Team, TeamAdmin)
