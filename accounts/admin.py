from django.contrib import admin
from .models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance')  # Fields to display in the list view

admin.site.register(Account)