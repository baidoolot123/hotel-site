from django.contrib import admin

# Register your models here.
from .models import RoomCategory, Rooms

admin.site.register(RoomCategory)
admin.site.register(Rooms)
