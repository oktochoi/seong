from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='main'),
    path('login/', views.login_view, name='login'),
    path('room/', views.room_view, name = 'room'),
    path('letter.html/', views.letter_view, name='letter'),
    path('present.html/', views.present_view, name='present'),
]
