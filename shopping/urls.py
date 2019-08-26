
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('account/', include('account.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('products/', include('commodity.urls')),
    path('orders/', include('order.urls')),
    path('admin/', admin.site.urls),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
