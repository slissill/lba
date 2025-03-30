from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('helloworld', views.helloworld, name='helloworld'),
]

'''
************************************************************
******* VENV ***********************************************
************************************************************

C:\ZLOCAL\VENV\SCRIPTS\activate.ps1
CD C:\ZLOCAL\lba\
python manage.py runserver


C:\ZDEPOT\VENV\SCRIPTS\deactivate


pip freeze > requirements.txt
pip install -r requirements.txt


'''