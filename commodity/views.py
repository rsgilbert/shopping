from django.shortcuts import render, get_object_or_404
from .models import Commodity

# Create your views here.


def commodities(request):
    if request.method == 'GET':
        items = Commodity.objects.all()
        return render(request, 'commodity/commodities.html', {'items': items})




