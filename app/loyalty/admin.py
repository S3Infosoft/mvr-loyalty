from django.contrib import admin



from .models import RewardItem,Guest,Hotels,Reservations,SpecialDeals,Profile,SpendPoints,ContactUs,Cart
# Register your models here.
admin.site.register(RewardItem)
admin.site.register(Guest)
admin.site.register(Hotels)
admin.site.register(SpendPoints)
admin.site.register(Reservations)
admin.site.register(SpecialDeals)
admin.site.register(Profile)
admin.site.register(ContactUs)
admin.site.register(Cart)

