from django.db.models.signals import post_save
from users.models import CustomUser
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		



@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
	if kwargs['created']==True:#at the time of login also this is being called ,that time created==false
		instance.profile.save()


    #automatically saved users profile picture while succesfull registration of user