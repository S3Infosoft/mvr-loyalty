from django.db import models

# Create your models here.
class PurchaseOrder(models.Model):

	razorpay_payment_id=models.CharField(max_length=100)
	razorpay_order_id=models.CharField(max_length=100)
	razorpay_signature=models.CharField(max_length=500)
	user_unique_id=models.CharField(max_length=40)
	user_email=models.EmailField(max_length=30)
	amount_debited=models.FloatField(max_length=20)
	points_added=models.IntegerField()
	
	def __str__(self):
		return self.user_email


