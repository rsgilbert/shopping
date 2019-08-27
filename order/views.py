from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from commodity.models import Commodity

# Create your views here.

def place_order(request, id):
    if request.method == "GET":
        commodity = get_object_or_404(Commodity, pk=id)
        form = OrderForm(initial={"commodity": commodity})
        return render(request, 'order/place_order.html', {'form': form, "id": id})

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commodity:commodities')
