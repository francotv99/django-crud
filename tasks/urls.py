from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estados/<int:pais_id>/', views.lista_estados, name='estados'),
    path('editarestados/<int:estado_id>/', views.editarestados, name='editarestados'),
    path('eliminarestado/<int:estado_id>/', views.eliminarestado, name='eliminarestado'),
    path('editarpais/<int:pais_id>/', views.editarpais, name='editarpais'),
    path('eliminarpais/<int:pais_id>/', views.eliminarpais, name='eliminarpais'),
]
