from django.db import models


from post.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Tag(models.Model):
    title=models.CharField(max_length=150)
    slug=models.SlugField(blank=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title





def tag_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_save,sender=Tag)