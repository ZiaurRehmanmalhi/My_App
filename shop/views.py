from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides': nSlides, 'range': range(nSlides), 'product': products}
    return render(request, 'shop/index.html')
    # return HttpResponse("Index shop")


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("we are contact")


def tracker(request):
    return HttpResponse("we are tracker")


def search(request):
    return HttpResponse("we are search")


def productview(request):
    return HttpResponse("we are productview")


def checkout(request):
    return HttpResponse("we are checkout")
