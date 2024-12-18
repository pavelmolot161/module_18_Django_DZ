
from django.shortcuts import render

from django.views.generic import TemplateView

### - 18.12.24 (+)

def menu_task(request):
    context = {                                                                 ### - (+)
        'games': ["Atomic Heart", "Cyberpunk 2077"]
    }
    return render(request, "fourth_task/menu.html", context)

def platform_task(request):
    return render(request, "fourth_task/platform.html")

def games_task(request):
    return render(request, "fourth_task/games.html")

def cart_task(request):
    return render(request, "fourth_task/cart.html")


###################################################################











