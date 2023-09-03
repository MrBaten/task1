
from django.shortcuts import render
from .models import Trade

def home(request):
    trades = Trade.objects.all()
    return render(request, 'myapp/home.html', {'trades': trades})