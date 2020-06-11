from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Product
from .forms import ProdutoForm


def list_products(request):
    #reverse('produtos:list', current_app=request.resolver_match.namespace)

    p = Product.objects.all()
    context = {
        'products': p
    }
    return render(request, 'products/list.html', context=context)


def create_product(request):
    #reverse('produtos:create', current_app=request.resolver_match.namespace)

    if request.method == "POST":
        form = ProdutoForm(request.POST)
        valido = form.is_valid()
        if valido:
            form.save()
            form = ProdutoForm()
            return redirect("produtos:list")

    else:
        # metodo GET
        form = ProdutoForm()

    context = {
        'form': form
    }

    return render(request, 'products/create.html', context)


def update_product(request,id):
    pdt = Product.objects.get(pk=id)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=pdt)
        valido = form.is_valid()
        if valido:
            form.save()
            return redirect("produtos:list")

    else:
        # metodo GET
        form = ProdutoForm(instance=pdt)

    context = {
        'form': form
    }

    return render(request, 'products/update.html', context)


def delete_product(request, id):
    pdt = Product.objects.get(pk=id)
    pdt.delete()
    return redirect("produtos:list")
