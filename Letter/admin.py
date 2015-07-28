from django.contrib import admin
from .models import Letter


class LetterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'date_created', 'date_received')
    list_filter = ['date_created']
    search_fields = ['subject']

admin.site.register(Letter,LetterAdmin)

# Register your models here.
