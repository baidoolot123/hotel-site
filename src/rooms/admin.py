from django.contrib import admin

# Register your models here.
from .models import RoomCategory, Rooms, Services, RoomPhoto

class RoomPhotoAdmin(admin.TabularInline):
    
    model = RoomPhoto


class RoomsAdmin(admin.ModelAdmin):
    list_display = ['name', 'room_category', 'price']
    search_fields = ['name', 'room_category']
    list_filter = ['room_category', 'price']
    inlines = [RoomPhotoAdmin]

admin.site.register(RoomCategory)
admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Services)
#admin.site.register(RoomPhoto)


