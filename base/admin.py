from django.contrib import admin

from .models import Room , Topic , Message , User

# Register your models here.

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ('username',)
admin.site.register(Room)
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    search_fields = ["name"] 
admin.site.register(Message)