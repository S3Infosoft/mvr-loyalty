from django.db import models

# Create your models here.
class RewardItem(models.Model):
	item_name=models.CharField(max_length=50)
	item_price=models.FloatField(max_length=10)
	item_description=models.TextField()
	points_required=models.IntegerField()

	def __str__(self):
		return f'{self.item_name }'

class Guest(models.Model):
	name=models.CharField(max_length=50)
	phone=models.IntegerField()
	email=models.EmailField(max_length=30,blank=True)
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
	contact_p_phone=models.IntegerField()
	reward_ratio=models.FloatField(max_length=30)

	def __str__(self):
		return f'{self.name }'


class Reservations(models.Model):
	guest=models.ForeignKey(Guest,on_delete=models.CASCADE)
	hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE)
	v_t_hotel=models.DecimalField(max_digits=10, decimal_places=2)#(by this reservation only)
	points_obtain=models.IntegerField()#from this reservation only(v_t_hotel * hotel.reward ratio)


	def __str__(self):
		return f'reservation of {self.guest }'






