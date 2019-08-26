from django.urls import path
from . import views

app_name = 'commodity'


urlpatterns = [
    path('', views.commodities, name='commodities'),
    path('<int:id>', views.commodity, name="commodity"),
]