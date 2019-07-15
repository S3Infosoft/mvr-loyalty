from loyalty.models import Cart
import django
def messagenumber_processor(request):


	if not request.user.is_anonymous:#when logout user is anonymous
		return {'total_cart_items': len(Cart.objects.filter(user__unique_id=request.user.unique_id))}
	else:
		return{'temp': None}

#we can access this 'total_cart_items' into any template by {{total_cart_items}} without passing it from view
#when we have something which is pass everytime to each template from each view ..we do this..instead of passing
#from each view

#we have to add this method to settings.py
#in TEMPLATES-->context_processors