from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.eventoList, name = 'eventoList'),
    path('eventoCreate/', csrf_exempt(views.evento_create), name = 'eventoCreate'),
]