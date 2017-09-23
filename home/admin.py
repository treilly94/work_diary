from django.contrib import admin

from .models import Account
import datetime


class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'date_of_birth', 'creation_date')
    list_filter = ['location']
    search_fields = ['user', 'location', 'date_of_birth', 'creation_date']
    ordering = ['-creation_date']

    def save_model(self, request, obj, form, change):
        obj.creation_date = datetime.datetime.today()
        obj.modified_date = datetime.datetime.today()
        obj.save()

admin.site.register(Account, AccountAdmin)