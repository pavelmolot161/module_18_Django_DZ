#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UrbanDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#####################################################################################################


### - 14.12.24
### - Эта команда вернет на один уровень выше в адресной строке:
#                                                            >>> cd ..

### - 1) установка Django: - (.venv) PS D:\module_18_Django> >>> pip install django

### - 2) Убедимся, что установка Django прошла успешно (не обязательно):
#                            (.venv) PS D:\module_18_Django> >>> python

### - 3) узнаем версию Django:                               >>> django.get_version()

### - 4) Создание проекта: - (.venv) PS D:\module_18_Django> >>> django-admin startproject mysite

### - 5) создание таблиц в базе данных для всех приложений из списка INSTALLED_APPS:
#                            (.venv) PS D:\module_18_Django> >>> cd mysite
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py migrate

### - 6) ЗАПУСK серверa разработки:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py runserver

### - 7) Создание приложения:
#                     (.venv) PS D:\module_18_Django\mysite> >>> python manage.py startapp app

### - 8) Создание файла зависимостей:
#             (.venv) PS D:\module_18_Django_DZ\UrbanDjango> >>> pip freeze > requirements.txt
#     8.a) вывод зависимостей в консоль:
#                                                            >>> pip freeze

'''Выполнен 1 пункт выполнен, 2 пункт выполнен, 3 пункт - не сработал, 4 пункт выполнен,
            7 пункт выполнен - создано 3 приложения с названиями 'example1', 'example2', 'example3'
            8 пункт выполнен - создан файл зависимостей requirements.txt.
            8 пункт выполнен сработал.
           '''

### - 15.12.24
### - 9) Создали приложение - task2
### - 10) Создали папку templates и в ней папку second_task:
##        - создаем 2 HTML шаблона - class_template.html, func_template.html

### - 11) В приложении task2 в файле views.py добавили:
##                   def func_temp(request):
#                       return render(request, "func_template.html")
#
#                    class class_temp(TemplateView):
#                       template_name = "class_template.html"

### - 15.12.24
### - Поменял структуру проэкта и определил корневую папку UrbahDjango.
                        # 1- Откройте PyCharm.
                        # 2 - Перейдите в меню File -> Open....
                        # 3 - Выберите папку, которую хотите установить в качестве корня проекта.
                        # 4 - PyCharm автоматически установит выбранную папку как корень проекта.

### - 12) Внесение дополнений в папку UrbahDjango файл urls.py:
                        # urlpatterns = [
                        #     path('admin/', admin.site.urls),
                        #     path('', func_temp),
                        #     path('class_temp_sample/', class_temp.as_view())]

### - 13) ЗАПУСK НОВЫЙ серверa разработки, (выполнив команду из корневого каталога проекта):
#                     PS D:\module_18_Django_DZ\UrbanDjango> >>> python manage.py runserver

### - 14) Созданs 2 новых файла HTML в папке templates c названием class_template.html, func_template.html,


