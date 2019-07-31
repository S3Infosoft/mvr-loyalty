from django.db import models
from django.contrib.auth import base_user, models as auth_models
from django.utils.translation import ugettext_lazy as _
import uuid


class CustomUserManager(base_user.BaseUserManager):
    """
    CustomUser manager for CustomUser for authentication using email and
    password
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create a user with given email and password
        """
        #print("Inside Custom_create"*5)
        if email:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)

            return user

        raise ValueError(_("Email must entered to create a user"))

    def create_superuser(self, email, password, **extra_fields):
        """
        Create a superuser with given email, password and other credentials
        """
        #print("Inside_superuser"*5)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("Superuser must have is_staff=True"))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must have is_superuser=True"))

        return self.create_user(email, password, **extra_fields)


class CustomUser(auth_models.AbstractUser):#whatever field you want extra in user model we can enter here
    """
    CustomUser model with email and password for authentication

    """
    #print("Inside CustomUser"*5)

    
    points_available=models.FloatField(max_length=10,default=0.0)
    unique_id=models.CharField(max_length=40,null=True,blank=True,unique=True,default=uuid.uuid4)
    phone= models.CharField(max_length=12,blank=True,null=True)
    



   #this 3 fields username and points_available are added to our user model
    ##whatever ectra fields are added in CustomUser model ,to show it in admin panel,we have to
    #add that in admin.py
   

    email = models.EmailField(_("email address"), unique=True)

    
    objects = CustomUserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

#whenever new user created either superuser form CLI or from normal user from login page,
#user gets this all fields, available in CustomUser class
#when we start server, this class automatically called and all fields are created before creating new user itself
#CutsomUser class is model here but CustomUSerManger is not model it is only class which is called from 
#CustomUser for creating superuser fields
#from shell we can check all fields of this CustomUser model by CustomUser._meta.fields 

#there is relatioship between this CustomUser model and User model..
#now all objects can be accessible by CustomUser model only by CustomUser.objects.all()
#we can not access User model like User.objects.all() it gives error
#if we check User._meta.fields then it doesnot have this extra 2added fields as well


