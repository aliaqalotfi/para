from django.urls import path
from . import views
app_name='post'
urlpatterns = [
    path('', views.post_list_view,name="list"),
    path('search', views.search,name="search"),
    path('tag/<slug>', views.tag,name="tag"),
    path('create', views.post_create,name="create"),
    path('create_form', views.create_form,name="create_form"),
    path('edit/<pk>', views.edit,name="edit"),
    path('delete/<pk>', views.delete,name="delete"),

    path('<slug>', views.post_detail_view,name="detail"),

]