from django.contrib import admin
from .models import Poll, Option

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3

# Register your models here.
class PollAdmin(admin.ModelAdmin):
    list_display = ('title','date_created','was_published_recently')
    list_filter = ['date_created']
    search_fields = ['title']
    
    fieldsets = [
        ( None, { 'fields': ["title"] } ),
        ( "Description of the Poll", { 'fields': ["content"], 'classes': ['collapse'] } ),
        ( "Publish date", { 'fields': ["date_created"], 'classes': ['collapse'] } )
    ]
    inlines = [OptionInline]


admin.site.register(Poll, PollAdmin)