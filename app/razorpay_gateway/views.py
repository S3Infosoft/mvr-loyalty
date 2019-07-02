from django.shortcuts import render,redirect
from .forms import PurchasePointsForm
from django.contrib.auth import decorators
from django.views.decorators.csrf import csrf_exempt
from .models import PurchaseOrder
from django.http import Http404#everytime i need to import wherever i use..otherwise gives error
from users.models import CustomUser
from config import settings

@decorators.login_required
def checkout(request):
	
    
	if request.method=='POST' and request.user.unique_id== request.POST['security_value']:
		print(request.POST['Enter_Points_to_be_purchase'])
		print(request.POST['security_value'])
		import razorpay
		client=razorpay.Client(auth=(settings.razorpay_key_id , settings.razorpay_secret_id ))
		#resp = client.order.fetch_all()
		DATA = {
		"amount": float(request.POST['Enter_Points_to_be_purchase'])*100,
		"currency": "INR",
		"notes": {"ok":"hiiiiii nothing"},
		"payment_capture" : 0 #its good not to capture payment here ,bcoz it may happen that  
		                      #after completion of sucessful payment due to any issues 
		                      #payment info not saved in our database
		                      #then there is ambuguity if we capture here itself
		                      #it may happen that payment is capture but payment info is not store
		                      #in our database,in such cases if we keep 0 then it is not captured and
		                      #refund will process automatically since t capture after 5 days from razorpay
		}
		order_response=client.order.create(data=DATA)

		print("#"*10)
		print(order_response)

		context={
		"order_response_id":str(order_response['id']),
		"email":request.user.email,
		"name":request.user.get_full_name
		}

		return render(request, "razorpay/checkout.html",context)
	
	from django.http import Http404
	raise Http404("not found")        


@decorators.login_required
@csrf_exempt#it allows not check csrf token while recieving POST request
def checkout_done(request):
    
    if request.method=='POST':
      print("@@@"*10)
      print(request.POST)

      import razorpay
      client=razorpay.Client(auth=(settings.razorpay_key_id , settings.razorpay_secret_id ))
      for i in range(10):#10 trials if error occurs
        try:
          resp1=client.payment.fetch(request.POST['razorpay_payment_id'])#sometime error due to network or other error
          break
        except:
          pass

      if not type(resp1)==dict:
      	from django.http import Http404
      	raise Http404("payment failed...try again...your debited money will be refunded within 5 days")
      	

      


      amount_debited=resp1['amount']/100
      
      try:
          p_obj=PurchaseOrder(
          razorpay_payment_id= request.POST['razorpay_payment_id'],
          razorpay_order_id= request.POST['razorpay_order_id'],
          razorpay_signature= request.POST['razorpay_signature'],
          
          user_unique_id=request.POST['user_unique_id'],
          amount_debited=amount_debited,
          points_added=amount_debited,  
          user_email= request.POST['user_email'],
          )
          p_obj.save()
      except:
      	#if unable to save payment info into our database...e would not capture payment
      	#and it will be refunded automatically by razorpay in 5 days since not captured
      	from django.http import Http404
      	raise Http404("payment failed...try again...your debited money will be refunded within 5 days")

      
      for i in range(10):#10 trials if error occurs
        try:
          resp2 = client.payment.capture(request.POST['razorpay_payment_id'],resp1['amount'])#sometime error due to network or other error
          #this resp2 have all the information about payment evrything
          break
        except:
          pass

      if not type(resp2)==dict:
      	from django.http import Http404
      	raise Http404("payment failed...try again...your debited money will be refunded within 5 days")



      c_obj=CustomUser.objects.filter(unique_id=request.POST['user_unique_id']).first()
      c_obj.points_available=c_obj.points_available+amount_debited
      c_obj.save()
      
      from django.contrib import messages
      messages.success(request, f'Payment of Rs.{amount_debited} is sucessfull')    
      	

      return redirect("/coupens/")

    from django.http import Http404
    raise Http404("not found") 


@decorators.login_required
def purchase_points(request):

    security_value=request.user.unique_id
    form=PurchasePointsForm()
    myform={
         'form':form,
         'security_value': security_value

        }

    return render(request, "razorpay/purchase_points_form.html",myform)