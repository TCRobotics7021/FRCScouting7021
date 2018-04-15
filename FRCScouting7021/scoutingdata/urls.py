from django.urls import path
from . import views

app_name = 'scoutingdata'
 
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('user/<username>', views.user, name='user'),
]
