from . import views

from django.contrib.auth import views as auth_views
from django.urls import path, include
from loyalty import views as loyalty_views
from .views import earn_Points_History_Listview,spend_Points_History_Listview

password_urls = [
    path("change/done/", auth_views.PasswordChangeDoneView.as_view(),
         name="password_change_done"),
    path("change/", views.PasswordChangeView.as_view(),
         name="password_change"),
    path("reset/done/", auth_views.PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path("reset/complete/", auth_views.PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
    path("new/<uidb64>/<token>/",
         views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("reset/", auth_views.PasswordResetView.as_view(),
         name="password_reset"),
]

urlpatterns = [
    path("", views.my_Redirect, name="my_redirect"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("password_", include(password_urls)),
    path("coupens/", views.index, name="index"),
    path("deals/", views.deals, name="deals"),
    path("profile/",loyalty_views.profile,name="profile"),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("earn_history/",earn_Points_History_Listview.as_view(),name="earn_history"),
    path("spend_history/",spend_Points_History_Listview.as_view(),name="spend_history"),

]
