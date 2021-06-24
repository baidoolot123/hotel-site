from django.shortcuts import render
from .models import RoomCategory, Rooms
from reservation.models import Reservation
from reservation.forms import ReservationForm

def homepage(request):
    template = 'rooms/index.html'
    context = {
        'homepage': homepage
    }
    return render(request, template, context)
    
def rooms_list(request): 
    rooms_list = Rooms.objects.all()
    template = 'rooms/list.html'
    context = {
        'rooms_list' : rooms_list
    }

    return render(request, template, context)

def rooms_detail(request, id):
    rooms_detail = Rooms.objects.get(id=id)
    template = 'rooms/detail.html'

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
        
    else:
        reservation_form = ReservationForm()


    context = {
        'rooms_detail': rooms_detail,
        'reservation_form': reservation_form
        }
    return render(request, template, context)