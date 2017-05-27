from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    context = {
    'products': Product.objects.all()
    }
    return render(request, 'Shop/index.html', context)

def addProduct(request):
    return render(request, 'Shop/add_product.html')

def createProduct(request):
    if request.method == 'POST':
        Product.objects.create(name = request.POST['product_name'], description = request.POST['product_desc'], price = request.POST['product_price'])
    return redirect('/')

def updateProduct(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id = id)
        product.name = request.POST['product_name']
        product.description = request.POST['product_desc']
        product.price = request.POST['product_price']
        product.save()
    return redirect('/')

def showProduct(request, id):
    context = {
    'products': Product.objects.get(id = id)
    }
    return render(request, 'Shop/view_product.html', context)

def editProduct(request, id):
    context = {
    'products': Product.objects.get(id = id)
    }
    return render(request, 'Shop/edit_product.html', context)

def removeProduct(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return redirect('/')
