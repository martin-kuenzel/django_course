from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','date_created','date_updated','was_created_recently','was_updated_recently')
    list_filter = ['date_created','author']
    search_fields = ['title']

    fieldsets = [
        ( None, { 'fields': ['author'] } ),
        ( None, { 'fields': ['title'] } ),
        ( 'Erstellungsdatum', { 'fields': ['date_created'], 'classes': ['collapse'] } ),
        ( 'Aktualisierungsdatum', { 'fields': ['date_updated'], 'classes': ['collapse'] } ),
        ( 'Inhalt', { 'fields': ['content'] } )
    ]


# Register your models here.
admin.site.register(Post,PostAdmin)