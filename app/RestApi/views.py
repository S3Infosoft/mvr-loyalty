from django.shortcuts import render


import json
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.parsers import FileUploadParser

from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse

from .serializers import ReservationsSerializer,GuestSerializer, HotelsSerializer,ReservationsSerializer

from loyalty.models import Reservations,Guest,Hotels
from users.models import CustomUser
import uuid
from django.core.mail import send_mail
import os
from config import settings
import random

'''class ReservationsAPIView(APIView):
    def get(self, request):
        Reservations = Reservations.objects.all()
        serailizer = ReservationsSerializer(Reservations, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = ReservationsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)'''

class ReservationsViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationsSerializer
    queryset = Reservations.objects.all()

class GuestViewSet(viewsets.ModelViewSet):
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()




class GuestDetail(APIView):

    def get_object(self, id):
        try:
            return Guest.objects.get(id=id)
        except Guest.DoesNotExist as e:
            return 0

    def get(self, request, id=None):
        instance = self.get_object(id)
        if instance:
            serailizer = GuestSerializer(instance)
            return Response(serailizer.data)
        else:
            return JsonResponse( {"error": "Given Guest object not found."}, status=404)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        if instance:
            serializer = GuestSerializer(instance, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        else:
            return JsonResponse( {"error": "Given Guest object not found."}, status=404)


    def delete(self, request, id=None):
        instance = self.get_object(id)
        if instance:
            instance.delete()
            return HttpResponse(status=204)
        else:
            return JsonResponse( {"error": "Given Guest object not found."}, status=404)


class GuestAPIView(APIView):

    def get(self, request):
        questions = Guest.objects.all()
        serailizer = GuestSerializer(questions, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):
        data = request.body
        data=json.loads(data)#converts json data into dict
        g_obj=Guest.objects.filter(unique_id=data['unique_id'])

        if len(g_obj)==0:
            print("initiate create_user")
            user_obj=CreateUser()
            p=user_obj.create_user(data)
            if p==0:
                return JsonResponse( {"error": "can't create account in loyalty app"}, status=404)
            else:
                print("all done create_user")
                return Response(data, status=201)   
            
        else:
            guest_obj=g_obj.first()
            serializer = GuestSerializer(guest_obj)
            data=serializer.data
            data['status']="guest alreday exist in loyalty app"

            return JsonResponse(data, status=201)

class CreateUser():#User,Profile,Guest everything will be created once user is created
                   #user should be created with unique_id of guest of payment_tracker app
                   #so that while craeting user,customuser unique_id and guest unique id in loyalty
                   #will be same while creating
                   #again when reservation of that guest syncs,guest already existed will be shown

    def create_user(self,data):
        
        try:#have to create user like this ,if we crate using CustomUser() then password not craeted by django
            user, created = CustomUser.objects.get_or_create(first_name=data['first_name'],last_name=data['last_name'],email=data['email'],phone=data['phone'],unique_id=data['unique_id'],username=data['first_name']+data['last_name']+str(random.randrange(101,5000)))
            if created:
                password=uuid.uuid4()
                user.set_password(password)
                user.save()
                print("inside create_user")
                q=self.mail_send(data['email'],password)
                return q
        except:
            return 0
        
    


    def mail_send(self,email,password):
        try:
            print("inside mail send ")
            subject='account is created at www.loyalty.com '

            email_message=f"account with Email:- {email} is created, login with temporary password  {password}  and change it once logged in"
            from_email=settings.EMAIL_HOST_USER 
            recipients_list=[settings.recipients]#[request.user.email]
            send_mail(subject,email_message,from_email,recipients_list)
            print("mail sentttttt")
            return 1
        except:
            return 0





class HotelsAPIView(APIView):

    def get(self, request):
        h_objects = Hotels.objects.all()
        serailizer = HotelsSerializer(h_objects, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):

        data = request.body
        data=json.loads(data)#converts json data into dict
        h_obj=Hotels.objects.filter(unique_id=data['unique_id'])
        

        if len(h_obj)==0:
            
            serializer = HotelsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=404)
        else:

            hotel_obj=h_obj.first()
            serializer = HotelsSerializer(hotel_obj)
            data=serializer.data
            data['status']="hotel alreday exist in loyalty app"

            return JsonResponse(data, status=201)

class ReservationsAPIView(APIView):

    def get(self, request):
        r_objects = Reservations.objects.all()
        serailizer = ReservationsSerializer(r_objects, many=True)
        return Response(serailizer.data, status=200)

    def post(self, request):

        data = request.body
        data=json.loads(data)#converts json data into dict
        g_obj=Guest.objects.filter(unique_id=data['guest_unique_id']).first()#recently created
        h_obj=Hotels.objects.filter(unique_id=data['hotel_unique_id']).first()
        
        r_data={

             'guest':g_obj.id,#here we have to provide primary key,instead of just obj
             'hotel':h_obj.id,
           'v_t_hotel':data['v_t_hotel'],
            'date':data['date'],
            'points_obtain':data['points_obtain'],
        }

        serializer = ReservationsSerializer(data=r_data)
        if serializer.is_valid():
            serializer.save()
            data=serializer.data
            u=UpdateBalance()
            u.update_balance(data,g_obj)
            

            return Response(data, status=201)
        return Response(serializer.errors, status=404)


class UpdateBalance():

    def update_balance(self,data,guest_obj):
        c=CustomUser.objects.filter(unique_id=guest_obj.unique_id).first()
        c.points_available=c.points_available + data['points_obtain']
        c.save()
        
       

        
