from django.urls import path
from . import views

# Sätt upp all URL för sidan
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>', views.room, name="room"),
    path('create_room/', views.create_room, name="create_room"),
    ]
