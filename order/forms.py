from django import forms
from .models import Order



class OrderForm(forms.Form):
        fullname = forms.CharField(max_length=100)
        telephone = forms.CharField(max_length=100)
        hall = forms.CharField(max_length=100)
        room_number = forms.CharField(max_length=10)
