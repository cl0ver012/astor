from django.urls import path

from . import views


app_name = 'page1'

urlpatterns = [
    path('', views.index, name='index'),
    path('team', views.team, name='team'),
]
