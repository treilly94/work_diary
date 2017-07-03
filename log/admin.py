from django.contrib import admin

from .models import Exp

class ExpAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'field')
    list_filter = ['user', 'field']
    search_fields = ['user', 'field']

admin.site.register(Exp, ExpAdmin)
