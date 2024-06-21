from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('luis/', views.luis, name='luis'),
    path('', views.home, name='home'),
]