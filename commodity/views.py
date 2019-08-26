from django.shortcuts import render, get_object_or_404
from .models import Commodity

# Create your views here.


def commodities(request):
    if request.method == 'GET':
        items = Commodity.objects.all()
        return render(request, 'commodity/commodities.html', {'items': items})




def commodity(request, id):
    if request.method == 'GET':
        item = get_object_or_404(Commodity, pk=id)
        return render(request, 'commodity/commodity.html', {'item': item, 'id': id})
    

def place_order(request)    

    if request.method == "POST":
