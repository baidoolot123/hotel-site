from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rooms'

urlpatterns = [
    path('', views.room_list, name='room_list')
]