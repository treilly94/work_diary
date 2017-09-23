from django.contrib import admin
from .models import WorkLog
import datetime


class WorkLogAdmin(admin.ModelAdmin):
    list_display = ('creation_date', 'author', 'title')
    list_filter = ['author', 'title']
    search_fields = ['author', 'title']
    ordering = ['-creation_date']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.creation_date = datetime.datetime.today()
        obj.modified_date = datetime.datetime.today()
        obj.save()

admin.site.register(WorkLog, WorkLogAdmin)
