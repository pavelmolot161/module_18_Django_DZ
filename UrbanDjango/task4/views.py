
from django.shortcuts import render

from django.views.generic import TemplateView

### - 18.12.24 (+)

context = {                                                                 ### - (+)
        'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]
    }
def menu_task(request):
    return render(request, "fourth_task/menu.html")

def platform_task(request):
    return render(request, "fourth_task/platform.html")

def games_task(request):
    return render(request, "fourth_task/games.html", context)

def cart_task(request):
    return render(request, "fourth_task/cart.html")
    #return render(request, "fourth_task/cart.html")

###################################################################











