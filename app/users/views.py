from .forms import RegisterForm


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views, decorators
from django.contrib.messages.views import SuccessMessageMixin
from loyalty.models import Guest,RewardItem,SpecialDeals,Reservations,SpendPoints
from users.models import CustomUser
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

def my_Redirect(request):
  return redirect("/coupens/")


@decorators.login_required
def index(request):
    #print(Guest.objects.filter(email=request.user).first())
    
  
    context={
           'users':CustomUser.objects.all(),
           'guests':Guest.objects.all(),
           'rewards':RewardItem.objects.all(),
           'current_user': CustomUser.objects.filter(email=request.user).first(),
           'current_user_points': CustomUser.objects.filter(email=request.user).first().points_available,
           #__ is used to access foreignkey fields in queryset
           #custom user and guest email must same
           'reservation': Reservations.objects.filter(guest__email=request.user.email),

          
                 }

    
    return render(request, "index.html",context)


@decorators.login_required
def deals(request):

    '''reservations=Reservations.objects.filter(guest__email=request.user.email)
    spend_points=SpendPoints.objects.filter(guest__email=request.user.email)
    sum_earn=0
    sum_spend_coupen=0
    sum_spend_deal=0

    for i in reservations:
      sum_earn=sum_earn+(i.points_obtain)
    for j in spend_points:
      if j.reward_item==None:
        sum_spend_deal=  sum_spend_deal+j.special_deals.points_required
      elif j.special_deals==None:
         sum_spend_coupen=sum_spend_coupen+j.reward_item.points_required
    total_spend=sum_spend_coupen+sum_spend_deal
    current_user_points=sum_earn-total_spend'''

    context={  
            'reservations':Reservations.objects.filter(guest__email=request.user.email),
            'spend_points':SpendPoints.objects.filter(guest__email=request.user.email), 
           'guests':Guest.objects.all(),
           'rewards':RewardItem.objects.all(),
           'deals': SpecialDeals.objects.all(),
           'current_user':  CustomUser.objects.filter(email=request.user).first(),
           'current_user_points': CustomUser.objects.filter(email=request.user).first().points_available,
           
                 }
    return render(request, "deals.html",context)




@decorators.login_required
def contact_us(request):
    
 
    context={
           'guests':Guest.objects.all(),
           'rewards':RewardItem.objects.all(),
           'deals': SpecialDeals.objects.all(),
           'current_user':  CustomUser.objects.filter(email=request.user).first(),
           'current_user_points': CustomUser.objects.filter(email=request.user).first().points_available,
          
                 }
    return render(request, "contact_us.html",context)




class earn_Points_History_Listview(LoginRequiredMixin,ListView):

    
    model = Reservations
    template_name = 'earn_points_history.html'  

    context_object_name = 'reservations'
    paginate_by=5

    def get_queryset(self):

      return Reservations.objects.filter(guest__email=self.request.user.email).order_by('-date')



class spend_Points_History_Listview(LoginRequiredMixin,ListView):

    
    model = SpendPoints
    template_name = 'spend_points_history.html'  

    context_object_name = 'spend_points'
    paginate_by=5

    def get_queryset(self):

      return SpendPoints.objects.filter(guest__email=self.request.user.email).order_by('-date')
        
                                                                          






class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = "users/login.html"
    success_url = reverse_lazy("index")
    success_message = "You are successfully logged in."
  




    def get(self, request, *args, **kwargs):
        # Prevent already login user from this page
        if self.request.user.is_authenticated:#it will be True if already login and try to access login page
            return redirect("/coupens/")

        return render(self.request,'users/login.html')


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
