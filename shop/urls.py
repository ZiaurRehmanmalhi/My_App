from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About_Us"),
    path("contact/", views.contact, name="contact_Us"),
    path("tracker/", views.tracker, name="tracking_status"),
    path("search/", views.search, name="search"),
    path("productview/", views.productview, name="productview"),
    path("checkout/", views.checkout, name="checkout")
]
