from django.contrib import admin
from models import Comic

class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date')

admin.site.register(Comic, ComicAdmin)
