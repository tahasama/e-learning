from django.contrib import admin
from .models import Message



#admin.site.register(Message)
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['author', 'course', 'timestamp']
    list_filter = ['author', 'course', 'timestamp']