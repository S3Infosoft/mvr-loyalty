from django.db import models
from django.contrib.auth.models import User
from config import settings
from users.models import CustomUser
from django.utils import timezone
import uuid

# Create your models here.
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
    # whenver user email changes guest email also should change
	name=models.CharField(max_length=50)
	phone= models.CharField(max_length=12)
	email=models.EmailField(max_length=30,blank=True)#guest email and custom user email must same
	address=models.TextField()
	points_available=models.IntegerField()


	def __str__(self):
		return f'{self.name }'

class Hotels(models.Model):

	name=models.CharField(max_length=50)
	image=models.ImageField(default='default.png',upload_to='hotels_pics')
	address=models.TextField()
	contact_p_name=models.CharField(max_length=50)
	contact_p_email=models.EmailField(max_length=30,blank=True)
	contact_p_phone=models.CharField(max_length=12)
	reward_ratio=models.FloatField(max_length=30)

	def __str__(self):
		return f'{self.name }'


class Reservations(models.Model):

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT)
	hotel=models.ForeignKey(Hotels,on_delete=models.PROTECT)
	v_t_hotel=models.DecimalField(max_digits=10, decimal_places=2)#(by this reservation only)
	points_obtain=models.IntegerField()#from this reservation only(v_t_hotel * hotel.reward ratio)
	date=models.DateTimeField(default=timezone.now)


	def __str__(self):
		return f'reservation of {self.guest }'


class SpecialDeals(models.Model):

	hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE)
	description=models.TextField()
	points_required=models.IntegerField()
	original_price=models.FloatField(max_length=10)


class SpendPoints(models.Model):
    #while creating new SpendPoint oject into data base
    #1of them is none
    #s=SpendPoints(date=timezone.now(),reward_item=None,special_deals=None)
    #s.save()

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT,null=True)
	date=models.DateTimeField(default=timezone.now)
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






