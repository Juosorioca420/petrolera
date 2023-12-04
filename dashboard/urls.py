from django.urls import path
from . import views 

urlpatterns = [ 
    path("", views.root_redirect, name = 'root_redirect'),
    path("home/", views.index, name = 'index'),  
    path("facturas/", views.facturas, name = 'facturas'),
    path("factura-delete-<str:pk>/", views.delete_factura, name = 'delete_factura'),
    path("inidicador/", views.indicador, name = 'indicador'),
    path("acta/", views.acta, name = 'acta'),
    path("campo/", views.campo, name = 'campo'),
    path("carrotanque/", views.carros, name = 'carrotanque'),
    path("oleoducto/", views.oleoducto, name = 'oleoducto'),
]
# name ->  href = '' a indicar en las vistas ->  '{% url 'name' %}'