from django.urls import path
from . import views

urlpatterns = [
    # Autores
    path('', views.diagnosticos_list, name='diagnosticos_list'),
    path('<str:diagnostico_id>/', views.diagnostico_detail, name='diagnostico_detail'),
    path('/uevo/', views.diagnostico_create, name='diagnostico_create'),

    # Publicaciones
    path('intentos', views.intentos_diagnosticos_list, name='intentos_diagnosticos_list'),
    path('<str:diagnostico_id>/', views.intento_diagnostico, name='diagnostico_intento'),
]
