from . import forms, models

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin



@admin.register(models.CustomUser)


#whatever ectra fields are added in CustomUser model ,to show it in admin panel,we have toadd that
#field here below in Fieldset




class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreateForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser

    list_display = ("email", "first_name", "last_name",
                    "is_staff", "is_active",)
    list_filter = "is_staff", "is_active",
    list_editable = "is_staff", "is_active",

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name",)}),


          (_("Extra added Fields "), {"fields": ("username", "points_available","phone","unique_id")}),

        

        (_("Permissons"), {"fields": ("is_staff",
                                      "is_active",
                                      "is_superuser",
                                      "groups",
                                      "user_permissions")}),
        (_("Important dates"), {"fields": ("date_joined", "last_login",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name",
                       "password1", "password2",
                       "is_active", "is_staff"),
        }),
    )

    search_fields = "email",
    ordering = "email",
