from django.shortcuts import redirect, render
from .models import Cliente
from .forms import CLiente_form
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


# Create your views here.
# @csrf_exempt

@login_required(login_url='/accounts/login/')
def pagina(request):
  return render(request,'core/pagina.html')


@login_required(login_url='/accounts/login/')
def cliente(request):
    client = Cliente.objects.all()
    datos = {
      "client": client
    }
    return render(request,'core/clientes.html',datos)
  #  return render(request,'core/clientes.html')

@csrf_protect
@login_required(login_url='/accounts/login/')
def form_cliente_del(request, id):
    client = Cliente.objects.get(identificacion=id)
    client.delete()
    return redirect(to="cliente")

@csrf_protect
@login_required(login_url='/accounts/login/')
def form_cliente(request):
    data = { 
     'form': CLiente_form()
    }
    if request.method == 'POST':
      formulario = CLiente_form(data=request.POST)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "Guardado Correctamente"
      else:
        #  data["form"] = formulario
         data["mensaje"] = "Error al Guardar los datos"
    return render(request,'core/cliente_formulario.html', data)
  # return render(request,'core/cliente_formulario.html')

@csrf_protect
@login_required(login_url='/accounts/login/')
def form_cliente_mod(request, id):
    client = Cliente.objects.get(identificacion=id)
    data = { 
     'form': CLiente_form(instance=client)
    }
    if request.method == 'POST':
      formulario = CLiente_form(data=request.POST,instance=client)
      if formulario.is_valid():
         formulario.save()
         data["mensaje"] = "Modificado Correctamente"
         data["form"] = formulario
      else:
         data["mensaje"] = "Error al Modificar los datos"
    return render(request,'core/cliente_formulario_mod.html', data)
