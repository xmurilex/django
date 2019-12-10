from django.shortcuts import render
from .forms import PedidoForm

def home(request):
    return render(request, 'home.html')

def post(request):
    return render(request, 'post.html')

def cadastro(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context = {
            'msg': "Pedido realizado com sucesso!"
    }

        return render(request, 'cadastro.html', context)
    context = {
        'formulario': form
    }
    return render(request, 'cadastro.html', context)


    