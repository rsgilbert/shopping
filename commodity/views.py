from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Commodity
from .forms import SearchForm

# Create your views here.


def commodities(request):
	if request.method == 'GET':
		items = Commodity.objects.all()
		form = SearchForm()
		return render(request, 'commodity/commodities.html', {'items': items, 'form': form})

	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			
			search_text = form.cleaned_data['text']
			print("Search word is ", search_text)    
			items = Commodity.objects.filter(name__icontains=search_text)
			return render(request, 'commodity/commodities.html', {'items': items, 'form': SearchForm()})

		else:
			print(form.errors)
			return HttpResponse(form.errors)
