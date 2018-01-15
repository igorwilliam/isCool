from django.contrib import admin

from .models import Topic, Reply
# Register your models here.

class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created', 'modified']
    search_fields = ['title', 'content']
    list_filter = ['created', 'modified']

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['content', 'created', 'modified']
    search_fields = ['content']
    list_filter = ['created', 'modified','topic']

admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
