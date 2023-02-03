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

def post(request, id):
    try:
        context = {
            'post': Blogpost.objects.get(id=id),
        }
        return render(request, 'post/post.html', context)
    except Blogpost.DoesNotExist:
        return render(request, 'post/post_not_found.html')