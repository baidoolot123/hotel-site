from django.urls import path
from . import views
from .views import rooms_list
from django.conf import settings
from django.conf.urls.static import static


app_name = 'rooms'

urlpatterns = [
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('<int:id>', views.rooms_detail, name='rooms_detail'),
    path('', views.homepage, name='homepage')
] 