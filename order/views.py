from django.shortcuts import render, get_object_or_404, redirect
from .forms import OrderForm
from commodity.models import Commodity
from .models import Order, OrderHistory

# Create your views here.


def place_order(request, id):
    commodity = get_object_or_404(Commodity, pk=id)
    print(request.method)
    if request.method == "POST":
        print("posting")
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                fullname=form.cleaned_data['fullname'],
                telephone=form.cleaned_data['telephone'],
                hall=form.cleaned_data['hall'],
                room_number=form.cleaned_data['room_number'],
                commodity=commodity
            )
            OrderHistory.objects.create(
                fullname=form.cleaned_data['fullname'],
                telephone=form.cleaned_data['telephone'],
                hall=form.cleaned_data['hall'],
                room_number=form.cleaned_data['room_number'],
                commodity=commodity
            )
            print("Valid")
            return render(request, 'order/place_order.html', {'form': form, "id": id, 'commodity': commodity, 'submitted': True})
        else:
            return render(request, 'order/place_order.html', {'form': form, "id": id, 'commodity': commodity })

    if request.method == "GET":
        form = OrderForm()
        print("getting")
        return render(request, 'order/place_order.html', {'form': form, "id": id, 'commodity': commodity, 'submitted': False})
