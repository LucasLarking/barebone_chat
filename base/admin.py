from django.contrib import admin

# Importera rum och meddelande och visa dem i admin-panelen
from .models import Room, Message
admin.site.register(Room)
admin.site.register(Message)
