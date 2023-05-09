from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
    # return HttpResponse("Index shop")


def about(request):
    return HttpResponse("we are about")


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
