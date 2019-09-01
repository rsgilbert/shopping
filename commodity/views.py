from django.shortcuts import render, get_object_or_404
from .models import Commodity

# Create your views here.


def commodities(request):
    if request.method == 'GET':
        items = Commodity.objects.all()
        return render(request, 'commodity/commodities.html', {'items': items})

    if request.method == "POST":
            print("Method was post", request.POST)
            searchword = request.POST['searchitem']
            print("Search word is ", searchword)    
            items = Commodity.objects.filter(name__icontains=searchword)
            return render(request, 'commodity/commodities.html', {'items': items})


