### - 15.12.24

from django.views.generic import TemplateView

                    # https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami ### - для папки templates (не трогать)
from django.shortcuts import render

# Create your views here. (Создавайте свои мнения здесь.)

### - requestrequest - запрос от пользователя
### - "index.html" - указываем шаблон который хотим вернуть

def func_temp(request):                                        ### - обработка логики и возврат шаблона пользователю
    return render(request, "func_template.html")

class class_temp(TemplateView):                                ### - класс наследуется от базового шаблона TemplateView
    template_name = "class_template.html"                      ### - Указывается имя нашего шаблона



