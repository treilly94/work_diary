from django.contrib import admin

from .models import Exp

class ExpAdmin(admin.ModelAdmin):
    list_display = ('creation_date', 'author', 'title')
    list_filter = ['author', 'title']
    search_fields = ['author', 'title']
    ordering = ['-creation_date']

admin.site.register(Exp, ExpAdmin)
