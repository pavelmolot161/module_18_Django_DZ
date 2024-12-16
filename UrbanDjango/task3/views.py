
from django.shortcuts import render
### - 16.12.24
from django.views.generic import TemplateView

def platform_task(request):
    return render(request, "third_task/platform.html")

def games_task(request):
    return render(request, "third_task/games.html")

def cart_task(request):
    return render(request, "third_task/cart.html")