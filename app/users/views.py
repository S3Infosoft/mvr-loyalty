from .forms import RegisterForm


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views, decorators
from django.contrib.messages.views import SuccessMessageMixin
from loyalty.models import Guest,RewardItem,SpecialDeals,Reservations,SpendPoints,ContactUs,Cart
from users.models import CustomUser
from razorpay_gateway.models import PurchaseOrder
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.views.generic import DeleteView
from django.core.mail import send_mail
from config import settings
import uuid
                                 




def my_Redirect(request):
  return redirect("/coupens/")


@decorators.login_required
def index(request):
   
    context={
           
           'rewards':RewardItem.objects.all(),
    
           'current_user_points': CustomUser.objects.filter(unique_id=request.user.unique_id).first().points_available,
           #__ is used to access foreignkey fields in queryset

           }

    
    return render(request, "index.html",context)


@decorators.login_required
def deals(request):

    context={  
           'deals': SpecialDeals.objects.all(),
           'current_user_points': CustomUser.objects.filter(unique_id=request.user.unique_id).first().points_available,
           
                 }
    return render(request, "deals.html",context)




@decorators.login_required
def contact_us(request):
  
  if request.method=='POST':

    c_obj=ContactUs(name=request.POST['Name'],
                     email=request.POST['Email'], 
                     subject=request.POST['Subject'],
                     message=request.POST['Message'],
                     user=request.user)
    c_obj.save()
    messages.success(request, f'your request subitted to our team,we will get back to you soon')
    return redirect('index')

  else:
    context={  'deals': SpecialDeals.objects.all(),
             }#not required
    return render(request, "contact_us.html",context)



@decorators.login_required
def cart(request):

  if request.method=="POST":

    if request.POST['reward_item_id'] !='0':

      reward_item_to_be_redeem=RewardItem.objects.filter(item_id=request.POST['reward_item_id']).first()
      c_obj=Cart(user=request.user,reward_items=reward_item_to_be_redeem,special_deals=None,status="pending")
      c_obj.save()
      request.user.total_cart_item = len(Cart.objects.filter(user__unique_id=request.user.unique_id))
      request.user.save()

    elif request.POST['special_deal_id'] !='0':

      special_deal_to_be_redeem=SpecialDeals.objects.filter(deal_id=request.POST['special_deal_id']).first()
      c_obj=Cart(user=request.user,reward_items=None,special_deals=special_deal_to_be_redeem,status="pending")
      c_obj.save()
      request.user.total_cart_item = len(Cart.objects.filter(user__unique_id=request.user.unique_id))
      request.user.save()

  context={
     'carts':Cart.objects.filter(user__unique_id=request.user.unique_id).order_by('-date'),
      'current_user_points': CustomUser.objects.filter(unique_id=request.user.unique_id).first().points_available,
     

    }

  return render(request, "cart.html",context)

  




@decorators.login_required
def Redeem(request):
  if request.method=='POST':
    g_obj=Guest.objects.filter(unique_id=request.user.unique_id).first()
    c_obj=Cart.objects.filter(cart_id=request.POST['cart_id']).first()

    if c_obj.reward_items != None and c_obj.special_deals == None :
      request.user.points_available=request.user.points_available - c_obj.reward_items.points_required
      request.user.save()

      subject='Coupen Successfully Redeemed'
      email_message="Your coupen is ........."
      from_email=settings.EMAIL_HOST_USER 
      recipients_list=['yashwadia7025@gmail.com']#[request.user.email]
      send_mail(subject,email_message,from_email,recipients_list)
            
      message="Coupens is Redeemed successfully and sent to your email_id as well as on your phone"
      c_obj.delete()
    else:
      request.user.points_available=request.user.points_available - c_obj.special_deals.points_required
      request.user.save()

      subject='Special Deal is Successfully Redeemed'
      email_message="Your deal is..........."
      from_email=settings.EMAIL_HOST_USER 
      recipients_list=['yashwadia7025@gmail.com']#[request.user.email]
      send_mail(subject, email_message, from_email,recipients_list)

      message="Specail deal is Redeemed successfully and sent to your email_id as well as on your phone"
      c_obj.delete()

    s_obj=SpendPoints(guest=g_obj,status="completed",reward_item=c_obj.reward_items,special_deals=c_obj.special_deals)
    s_obj.save()

    messages.success(request, message)

    return redirect('index')

  from django.http import Http404
  raise Http404("not found")        





  


class earn_Points_History_Listview(LoginRequiredMixin,ListView):

    
    model = Reservations
    template_name = 'earn_points_history.html'  

    context_object_name = 'reservations'
    paginate_by=5

    def get_queryset(self):
      r_objs=Reservations.objects.filter(guest__unique_id=self.request.user.unique_id).order_by('-date')
      
      if len(r_objs)!=0:
        return r_objs
      else:
        return [0]#this must be iterable thing..so we use list....when no history this will returned



class spend_Points_History_Listview(LoginRequiredMixin,ListView):

    
    model = SpendPoints
    template_name = 'spend_points_history.html'  

    context_object_name = 'spend_points'
    paginate_by=5

    def get_queryset(self):
      s_objs=SpendPoints.objects.filter(guest__unique_id=self.request.user.unique_id).order_by('-date')
      
      if len(s_objs)!=0:
        return s_objs
      else:
        return [0]#this must be iterable thing..so we use list....when no history this will returned

        
                                                                          

class purchase_Points_History_Listview(LoginRequiredMixin,ListView):

    
    model = PurchaseOrder
    template_name = 'purchase_points_history.html'  

    context_object_name = 'purchase_points'
    paginate_by=5

    def get_queryset(self):
      p_objs=PurchaseOrder.objects.filter(user_unique_id=self.request.user.unique_id).order_by('-date')
      
      if len(p_objs)!=0:
        return p_objs
      else:
        return [0]#this must be iterable thing..so we use list....when no history this will returned

        
class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cart
    success_url = '/cart/'
    
    def test_func(self):
        cart = self.get_object()
        if self.request.user.unique_id == cart.user.unique_id:
            return True
        return False



'''class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("index")
    success_message = "You are successfully logged in."
  




    def get(self, request, *args, **kwargs):
        # Prevent already login user from this page
        if self.request.user.is_authenticated:#it will be True if already login and try to access login page
            return redirect("/coupens/")

        return render(self.request,'users/login.html')'''

from django.contrib.auth.mixins import UserPassesTestMixin
class LoginView(SuccessMessageMixin,UserPassesTestMixin, views.LoginView):
  template_name = "users/login.html"
  success_message = "You are successfully logged in."

  def test_func(self):
    try:
      if self.request.user.is_authenticated:
        return False
    except:
      pass
    return True




class RegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "users/register.html"
    success_message = "You have been successfully registered," \
                      " login with your email and password."

    def get(self, request, *args, **kwargs):

        # Prevent already logged in user from this page
        if self.request.user.is_authenticated:
            return redirect("/")
        
        return super(RegisterView, self).get(request, *args, **kwargs)


class PasswordChangeView(SuccessMessageMixin, views.PasswordChangeView):
    success_message = "Your password has been successfully changed."


class PasswordResetConfirmView(SuccessMessageMixin,
                               views.PasswordResetConfirmView):
    success_message = "Your new password has been set," \
                      " login with email and new password."


