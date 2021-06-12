from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'product': products}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def search(request):
    return  HttpResponse("we're at search")

def tracker(request):
    return  HttpResponse("we're at tracker")

def product(request):
    return  HttpResponse("we're at product view")

def checkout(request):
    return  HttpResponse("we're at checkout")
