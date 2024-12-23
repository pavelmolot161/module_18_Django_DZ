"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin



### - 23.12.24 (+)


from task4.views import platform_task, games_task, cart_task, menu_task
from django.views.generic import TemplateView

# urlpatterns = [
#     path('', platform_task),
#     path('admin/', admin.site.urls),
#     path('menu', menu_task),
#     path('platform', platform_task),
#     path('games', games_task),
#     path('cart', cart_task),
# ]

urlpatterns = [                                        ### - (+)
    path('', platform_task, name='platform_task'),
    path('menu', menu_task, name='menu_task'),
    path('games', games_task, name='games_task'),
    path('cart', cart_task, name='cart_task'),
]