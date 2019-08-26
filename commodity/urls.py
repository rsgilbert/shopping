from django.urls import path
from . import views


urlpatterns = [
    path('', views.commodities, name='commodities'),
    path('<int:id>', views.commodity, name="commodity"),
]