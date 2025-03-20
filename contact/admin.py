from django.contrib import admin
from .models import ContactUs

@admin.register(ContactUs)
class Contact(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']