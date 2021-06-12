from django.shortcuts import render
from .models import RoomCategory, Rooms

def room_list(request):
    rooms = Rooms.objects.all()

    return render(request, 'rooms/index.html', {'rooms':rooms})
