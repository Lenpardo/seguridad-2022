from django.urls import path
from rest_proveedor.views import lista_proveedor , detalle_proveedor 
from rest_proveedor.viewsLogin import loginValidation

urlpatterns = [
    # path('lista_proveedor', lista_proveedor, name="lista_proveedor"),
    # path('detalle_proveedor/<id>', detalle_proveedor, name="detalle_proveedor"),
    # path('loginValidation', loginValidation, name="loginValidation"),
]
