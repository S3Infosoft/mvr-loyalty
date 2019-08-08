from django.db import models
from django.contrib.auth.models import User
from config import settings
from users.models import CustomUser
from django.utils import timezone
import datetime
import uuid

# Create your models here.

#when we assign field as blank=True ,then that field becomes optional
class RewardItem(models.Model):

	item_name=models.CharField(max_length=50)
	item_price=models.FloatField(max_length=10)
	item_description=models.TextField()
	points_required=models.IntegerField()
	item_image=models.ImageField(default='default_image.png',upload_to='reward_item_pics')
	item_id=models.CharField(max_length=1000, blank=True,null=True, unique=True, default=uuid.uuid4)

	def __str__(self):
		return f'{self.item_name }'

class Guest(models.Model):
    
	name=models.CharField(max_length=50)
	phone= models.CharField(max_length=12,blank=True,null=True)
	email=models.EmailField(max_length=30,blank=True)
	address=models.TextField(blank=True,null=True)
	#didnt make points_available field...we would get that from CustomUser database
	#guest unique_id and CutstomUSer unique_id should be same ,in loyalty app and  payment tracker app it should naver cahnge
	unique_id=models.CharField(max_length=500 ,unique=True, default=uuid.uuid4)

	def __str__(self):
		return f'{self.email }'

class Hotels(models.Model):

	name=models.CharField(max_length=50)
	image=models.ImageField(default='default.png',upload_to='hotels_pics',null=None,blank=True)
	address=models.TextField()
	contact_p_name=models.CharField(max_length=50)
	contact_p_email=models.EmailField(max_length=30,blank=True)
	contact_p_phone=models.CharField(max_length=12)
	reward_ratio=models.FloatField(max_length=30)
	unique_id=models.CharField(max_length=500, unique=True, default=uuid.uuid4)


	def __str__(self):
		return f'{self.name }'


class Reservations(models.Model):

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT)
	hotel=models.ForeignKey(Hotels,on_delete=models.PROTECT)
	v_t_hotel=models.FloatField(max_length=30)#(by this reservation only)
	points_obtain=models.IntegerField()#from this reservation only(v_t_hotel * hotel.reward ratio)
	#we have use this datefield bcoz datetime obj cannot pass throgh api..therefore converted in string
	date=models.CharField(max_length=50,default=timezone.now)
	unique_id=models.CharField(max_length=500, unique=True, default=uuid.uuid4)


	def __str__(self):
		return f'reservation of {self.guest }'


class SpecialDeals(models.Model):

	deal_name=models.CharField(max_length=100, blank=True, default="no name")
	hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE,null=True)
	description=models.TextField()
	points_required=models.IntegerField()
	original_price=models.FloatField(max_length=10)
	deal_image=models.ImageField(default='deal.jpg',upload_to='deals_pics')
	deal_id=models.CharField(max_length=1000, blank=True, default=uuid.uuid4)

	def __str__(self):
		return f'{self.deal_name }'


class SpendPoints(models.Model):
    #while creating new SpendPoint oject into data base
    #1of them is none
    #s=SpendPoints(date=timezone.now(),reward_item=None,special_deals=None)
    #s.save()

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT,null=True)
	date=models.CharField(max_length=50,default=timezone.now)
	#status---> rejectedor completed 
	status=models.CharField(max_length=50, blank=True)
	#guest will spend points in either one of below 2......1 field would be None
	#therefore i have set null=True
	reward_item=models.ForeignKey(RewardItem,on_delete=models.PROTECT,blank=True,null=True)
	special_deals=models.ForeignKey(SpecialDeals,on_delete=models.PROTECT,blank=True,null=True)

	def __str__(self):
		return f'{self.guest }'



class Profile(models.Model):
	user=models.OneToOneField(CustomUser,on_delete=models.CASCADE) #onetoone relationship..
	                                                          #1 user will ahve onlyone profilepic and image
	                                                          #we directly can use 
	                                                          #user=User.objects.all().first()
	                                                          #then directly can use user.profile.image.url
	                                                          #in profile.html it is used
	                                                          #profile will be object of Profile class
	                                                          #dont know how
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')

	def __str__(self):
		return f'{self.user} Profile'

#it has relationship with CustomUser we can access profile in shell like
#p=CustomUser.objects.filter(email="yashpatel7025@gmail.com").first()
#p.profile,p.profile.image
#p.profile._meta.fields
#here we cannnot make onetoone relationship with User insted of CustomUser bcoz User model already has
#relationship with CustomUser ....in settingswe have defined 
#AUTH_USER_MODEL = "users.CustomUser"
#IN SHORT we have EXTENDED fileds of User modelin CustomUser model so User model cannot be access with 
#User.objects.all()....now all USer fields aree accessible by CustomUSer


class ContactUs(models.Model):

	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=30)
	phone=models.CharField(max_length=15)
	subject=models.CharField(max_length=300)
	message=models.CharField(max_length=1000)
	user=models.ForeignKey(CustomUser,on_delete=models.PROTECT,null=True)

	def __str__(self):
		return f'from {self.user} '




class Cart(models.Model):

	user=models.ForeignKey(CustomUser,on_delete=models.PROTECT)
	reward_items=models.ForeignKey(RewardItem,on_delete=models.PROTECT,null=True,blank=True)
	special_deals=models.ForeignKey(SpecialDeals,on_delete=models.PROTECT,null=True,blank=True)
	status=models.CharField(max_length=50)
	date=models.DateTimeField(default=timezone.now)
	cart_id=models.CharField(max_length=1000, blank=True, default=uuid.uuid4)

	def __str__(self):
		return f'from {self.user} '


