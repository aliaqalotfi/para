from django.urls import path
from . import views
app_name="account_sys"
urlpatterns = [

    path('register', views.register_page,name="register"),
    path('login', views.login_page,name="login"),
    path('log_out', views.log_out,name="logout"),
]
