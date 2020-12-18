from django.contrib import admin

# Register your models here.
from my_tag.models import Tag

admin.site.register(Tag)