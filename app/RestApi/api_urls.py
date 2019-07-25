from django.contrib import admin
from django.urls import path,include

from . import views
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register('v1',views.ReservationsViewSet)
router.register('v2',views.GuestViewSet)



urlpatterns = [

     path('guest/<int:id>/', views.GuestDetail.as_view()),
     path('guest/', views.GuestAPIView.as_view()),
   
     path('hotel/', views.HotelsAPIView.as_view()),
     path('reservation/', views.ReservationsAPIView.as_view()),
     path('', include(router.urls)),

   

     
     ]


