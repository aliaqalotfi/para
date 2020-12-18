from django.urls import path
from . import views
app_name="account_sys"
urlpatterns = [

    path('register', views.register_page,name="register"),
]
