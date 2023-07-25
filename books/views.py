from django.shortcuts import render
from . import templates
import os
from .models import Post
from django import forms
from django.http import JsonResponse, HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
class createListingForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={"rows":1, "cols":115, "placeHolder":"Book Title", "maxlength": 50}), label="")
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":115, "placeHolder":"Book Title", "maxlength": 50}), label="")



def index(request):
    if request.method == "POST":
        postDetails = Post()
        postDetails.title = request.POST.get("title")
        postDetails.description = request.POST.get("description")
        postDetails.save()
        return HttpResponseRedirect("/")
    return render(request, "index.html", {"posts" : Post.objects})

def upload(request):
    return render(request, "upload.html", {"form" : createListingForm()})
    
@csrf_exempt 
def posts(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        itemid = data.get("id", "")
        Post.objects.get(id = itemid).delete()
        return render(request, "index.html", {"posts" : Post.objects})

    try:
        posts = Post.objects.all()
        revposts = []
        for post in posts:
            revposts.insert(0,post)
        
        return JsonResponse([post.serialize() for post in revposts], safe=False)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Posts not found."}, status=404)
