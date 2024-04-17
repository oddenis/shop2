from django.shortcuts import render
from .models import Products
from .forms import ProductForm

# Create your views here.

def products(request):
    prod = Products.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        dataProduct = ProductForm(request.POST)
        if dataProduct.is_valid():
            dataProduct.save()

    context = {'products':prod, 'form':form}

    return render(request, 'products/products.html', context)