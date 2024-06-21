from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [

     path('cristian/', views.cristian, name='cristian'),
     
    path('', views.home, name='home'),

]