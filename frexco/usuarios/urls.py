from django.urls import path
from usuarios import views

urlpatterns = [
    path('usuarios/',
         views.usuarios_lista,
         name='mostrar-usuarios'),
    path('usuarios/adiciona/',
         views.usuarios_salva,
         name='salvar-usuario'),
]
