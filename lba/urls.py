from django.urls import path
from . import views
urlpatterns = [
    path('', views.hello_world, name='home'),
    path('helloworld', views.helloworld, name='helloworld'),
]
