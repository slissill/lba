from django.urls import path
from . import views


app_name = "lba"

urlpatterns = [
    path('', views.home, name='home'),
    path('helloworld', views.helloworld, name='helloworld'),
    path('artist/<str:artist_name>/', views.artist, name='artist'),    
    path('album/<str:album_id>/', views.album, name='album'),    
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