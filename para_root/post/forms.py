from django import forms
from . import models
class create_post_form(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=["title","slug","body","image","active","count",'my_tags']
