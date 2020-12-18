from django.contrib.auth.models import User
from django.db import models
import os
import random
from django.db.models import Q



from .utils import unique_slug_generator
from django.db.models.signals import pre_save

from my_tag.models import Tag

#########################manager#####################################################
class PostManager(models.Manager):
    def active_posts(self):
        return self.get_queryset().filter(active=True)
    def get_by_slug(self,slug):
        qs=self.get_queryset().filter(active=True,slug=slug)
        if qs.count() == 1:
            return qs
        else:
            return None
    def search(self,q):
        lookup = Q(title__icontains=q) | Q(body__icontains = q) | Q(my_tags__title__icontains=q)
        return self.get_queryset().filter(lookup,active=True).distinct()



#################################image_url_maker##################################################

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"
###############Class main model#####################################################################################
class Post(models.Model):
    title=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(blank=True, unique=True)
    body=models.TextField()
    image=models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active=models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    count=models.IntegerField(default=1)

    my_tags=models.ManyToManyField(Tag,blank=True)
    objects=PostManager()
    class Meta:
        verbose_name = 'مطلب'
        verbose_name_plural = 'مطالب'

    def __str__(self):
        return self.title










#############################################slug########################################
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Post)

############################count==0##################baraye false kardan activ agar tedad az 1 kamtar shode
def post_pre_save_count(sender, instance, *args, **kwargs):
    if instance.count==0:
        instance.active=False

pre_save.connect(post_pre_save_count, sender=Post)