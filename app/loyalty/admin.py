from django.contrib import admin

# Register your models here.
from .models import RewardItem,Guest,Hotels,Reservations,SpecialDeals,Profile
# Register your models here.
admin.site.register(RewardItem)
admin.site.register(Guest)
admin.site.register(Hotels)
admin.site.register(Reservations)
admin.site.register(SpecialDeals)
admin.site.register(Profile)
