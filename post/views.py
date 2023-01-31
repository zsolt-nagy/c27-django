from django.shortcuts import render
from .models import Blogpost

def index(request):
    posts = Blogpost.objects.all()
    count = posts.count()
    context = {
        'count': count,
        'posts': posts,
    }
    return render(request, 'post/template.html', context)



  