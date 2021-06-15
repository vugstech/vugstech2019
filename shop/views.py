from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, contct
from math import ceil


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4)-(n//4))
    # params = {'product': products}
    # return render(request,'shop/index.html',params)
    if request.method == "POST":
        print(request)
        name = request.POST.get('name', '')
        phone = request.POST.get('contact', '')
        email = request.POST.get('email', '')
        desc = request.POST.get('anything', '')
        check1 = request.POST.get('check1', 'off')
        check2 = request.POST.get('check2', 'off')
        meeting= contct(name=name, phone=phone, email=email, desc=desc, check1=check1, check2=check2)
        meeting.save()
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def search(request):
    return HttpResponse("we're at search")


def tracker(request):
    return HttpResponse("we're at tracker")


def product(request):
    return HttpResponse("we're at product view")


def checkout(request):
    return HttpResponse("we're at checkout")


# def meeting(request):
#
#
#     return render(request, 'shop/index.html')
