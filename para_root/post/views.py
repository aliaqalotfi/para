from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .models import Post

from .forms import create_post_form
from django.contrib.auth.decorators import permission_required
from my_tag.models import Tag
from django.contrib import messages

# Create your views here.
################postlist##############################################################
def post_list_view(request):
    qs=models.Post.objects.active_posts().order_by("-time")

    context={
        "title":"posts",
        "posts":qs,

    }
    return render(request, "post/post_list_view.html", context)


class Bazdid:
    adadesh=0
###################post detail#######################################################
def post_detail_view(request,slug):


    detail_qs=models.Post.objects.get_by_slug(slug=slug)

######FOR TAGS
    my_post=Post.objects.filter(slug=slug)
    ####inja post ro gerfetam rokhr\tam to aliaqa
    aliaqa=list(my_post)[0]
    ####tamamtag haye poste ro gereftam
    tags_to_page=list(aliaqa.my_tags.all())




    context={
        "post":detail_qs,
        "tags_to_page":tags_to_page,
    }

    if detail_qs is None:
        raise Http404()

    Bazdid.adadesh+=1
    ####baraye kam shodan tedad bad az kharid
    if Bazdid.adadesh>2:
        me = models.Post.objects.get(slug=slug)
        me.count -= 1
        me.save()

    return render(request,"post/post_detail_view.html",context)

########create post#############################################################
def post_create(request):

    if request.method=="POST":
        title=request.POST.get("title")
        my_tags=request.POST.get("my_tag")
        splited=my_tags.split(",")
        body=request.POST.get("body")
        image=request._files.get("image")
        publisher=request.user
        active=request.POST.get("active")
        if active == "on":
            active=True
        else:active=False
        count=request.POST.get("count")
        count=int(count)
        Post.objects.create(title=title, body=body, active=active, count=count, publisher=publisher, image=image)
        thispost = Post.objects.get(title=title)
        list_tags_id=[]
        for i in splited:
            Tag.objects.create(title=i)
            this_tag=Tag.objects.get(title=i)
            list_tags_id.append(this_tag.id)


        for t in list_tags_id:
            thispost.my_tags.add(t)















    return render(request, "post/post_create.html", {})
################crate built in forms#######################################################
def create_form(request):
    create__form=create_post_form(request.POST,request.FILES )

    if create__form.is_valid():
        instance=create__form.save(commit=False)
        instance.publisher=request.user
        instance.save()
    else:create__form=create_post_form()
    context={
        "create_post_form":create__form

    }
    return render(request, "post/create_form.html",context)

####################edit##########################
def edit(request,pk):
    qs=get_object_or_404(Post, pk=pk)

    if request.method=="POST":
        form=create_post_form(request.POST,request.FILES,instance=qs)

        if form.is_valid():
            form.save()
    else:
        form=create_post_form(instance=qs)
    context={
        "form":form,
        'post':qs
    }

    return render(request, "post/post_edit.html",context)


####################delete##########################
@permission_required("blog.delete_post","log_in",raise_exception=True)
def delete(request,pk):
    qs=get_object_or_404(Post, pk=pk)

    if request.method=="POST":
        form=create_post_form(request.POST,instance=qs)

        if form.is_valid():
            qs.delete()
            return redirect("post:list")
    else:
        form=create_post_form(instance=qs)
    context={
        "form":form,
        'post':qs
    }

    return render(request, "post/post_delete.html",context)



##############################################search############################3


def search(request):
    q=request.GET.get("q")
    if q is not None:

       post=Post.objects.search(q)
    else:
        post=Post.objects.active_posts()

    context={
        "posts":post
    }

    return render(request,"post/search.html",context)

#################tag##############################
###in func mibare besafhe ii ke post hayy k on tago drn neshoon mide
def tag(request,slug):
    tag_get=Tag.objects.get(slug=slug)

    qs = models.Post.objects.filter(active=True, my_tags=tag_get)





    context={
        "posts":qs
    }
    return render(request,"post/post_list_view.html",context)
