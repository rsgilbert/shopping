
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('account/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('products/', include('commodity.urls')),
    path('admin/', admin.site.urls),
]
