from django.urls import path
from . import views

app_name = 'scoutingdata'

# /scouting/...

urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('team/<int:teamNum>', views.team, name='team'),
    path('event/<eventCode>', views.event, name='event'),
]
