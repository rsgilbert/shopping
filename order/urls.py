from django.urls import path
from . import views


app_name = 'order'

urlpatterns = [
    path('', views.place_order, name="place_order"),
]