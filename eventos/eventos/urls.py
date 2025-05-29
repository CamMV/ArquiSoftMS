from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'', views.EventoViewSet, basename='evento')

urlpatterns = [
    path('', include(router.urls)),
]