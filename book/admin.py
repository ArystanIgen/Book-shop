from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['genre']
    search_fields = ['genre']


class JournalAdmin(admin.ModelAdmin):
    list_display = ['type','publisher']
    search_fields = ['publisher']


admin.site.register(Book,BookAdmin)
admin.site.register(Journal,JournalAdmin)
