from django.urls import path
# from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from .views import pagina,cliente,form_cliente,form_cliente_mod,form_cliente_del
# from .viewsLogin import validacion

urlpatterns = [
 path('', pagina,name="pagina"),
 path('cliente_formulario', form_cliente,name="cliente_formulario"),
 path('cliente_formulario_mod/<id>', form_cliente_mod,name="cliente_formulario_mod"),
 path('cliente_formulario_del/<id>', form_cliente_del,name="cliente_formulario_del"),
 path('cliente', cliente,name="cliente"),
]
