from django.urls import path, include
from . import views
urlpatterns = [

    path("checkout/", views.checkout, name="checkout"),
    path("checkout_done/", views.checkout_done, name="checkout_done"),
    path("purchase_points/", views.purchase_points, name="purchase_points"),

]
