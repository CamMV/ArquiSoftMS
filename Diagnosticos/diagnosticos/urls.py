from django.urls import path
from . import views

urlpatterns = [
    # Autores
    path('diagnosticos/', views.diagnosticos_list, name='diagnosticos_list'),
    path('diagnosticos/<str:diagnostico_id>/', views.diagnostico_detail, name='diagnostico_detail'),
    path('diagnosticos/nuevo/', views.diagnostico_create, name='diagnostico_create'),

    # Publicaciones
    path('diagnosticos/intentos', views.intentos_diagnosticos_list, name='intentos_diagnosticos_list'),
    path('diagnosticos/<str:diagnostico_id>/', views.intento_diagnostico, name='diagnostico_intento'),
]
