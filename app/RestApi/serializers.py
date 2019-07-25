from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from loyalty.models import Reservations,Guest,Hotels


# Serializers define the API representation.

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ('guest', 'hotel', 'v_t_hotel', 'points_obtain','date')

    def create(self, validated_data):
    	print("*"*60)

    	return Reservations.objects.create(**validated_data)
    	
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'phone', 'email', 'address','unique_id','id')

    def create(self, validated_data):
    	print("*"*60)

    	return Guest.objects.create(**validated_data)
    	
class HotelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotels
        fields = ('name', 'image', 'address', 'contact_p_name', 'contact_p_email','contact_p_phone', 'reward_ratio', 'unique_id', 'id')

    def create(self, validated_data):
        print("*"*60)

        return Hotels.objects.create(**validated_data)

class ReservationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservations
        fields = ('guest', 'hotel', 'v_t_hotel', 'points_obtain', 'date', 'unique_id', 'id')

    def create(self, validated_data):
        print("*"*60)

        return Reservations.objects.create(**validated_data)