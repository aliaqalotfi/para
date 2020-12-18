from django.urls import path
from . import views
app_name="account_sys"
urlpatterns = [

    path('register', views.register_page,name="register"),
    path('login', views.login_page,name="login"),
    path('log_out', views.log_out,name="logout"),
    path('profile', views.profile,name="profile"),
    path('change_password', views.change_password,name="change_password"),
    path('profile_photo', views.profile_photo,name="profile_photo"),
]
