from django.urls import path
from . import views

urlpatterns = [
    # Autores
    path('', views.diagnosticos_list, name='diagnosticos_list'),
    path('nuevo/', views.diagnostico_create, name='diagnostico_create'),
    path('intentos', views.intentos_diagnosticos_list, ),
    path('<str:diagnostico_id>/', views.diagnostico_detail, name='diagnostico_detail'),
    path('diagnosticos/<uuid:diagnostico_id>/intento/', views.intento_diagnostico, name='intento_diagnostico')

]
