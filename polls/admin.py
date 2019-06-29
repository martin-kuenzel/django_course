from django.contrib import admin
from .models import Poll, Option, OptionSet

class OptionInline(admin.TabularInline):
    model = Option
    extra = 3

class OptionSetInline(admin.TabularInline):
    model = OptionSet
    extra = 1

class OptionSetAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     ("Optionen", { 'fields': ['option'] } )
    # ]
    inlines = [OptionInline]

class PollAdmin(admin.ModelAdmin):
    list_display = ('title','author','date_created','was_published_recently')
    list_filter = ['date_created','author']
    search_fields = ['title']
    
    fieldsets = [
        ( None, { 'fields': ["author"] } ),
        ( None, { 'fields': ["title"] } ),
        ( "Description of the Poll", { 'fields': ["content"], 'classes': ['collapse'] } ),
        ( "Publish date", { 'fields': ["date_created"], 'classes': ['collapse'] } )
    ]
    inlines = [OptionSetInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(OptionSet, OptionSetAdmin)