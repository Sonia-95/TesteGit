from django.urls import path
from .import views

urlpatterns = [
    path('', views.primeiraPagina, name='pagina1'),
    path('<int:clique_mouse>', views.pagina2, name='pagina2'),
    path('busca/', views.pesquisar, name='busca')
]
