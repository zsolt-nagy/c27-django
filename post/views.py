from django.shortcuts import render
from .models import Blogpost
import markdown


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
        context['html'] = markdown.markdown(context['post'].text) 
        return render(request, 'post/post.html', context)
    except Blogpost.DoesNotExist:
        return render(request, 'post/post_not_found.html')


def new_post(request):
    if request.method == 'POST':
        # save the post in the database
        try:
            new_post = Blogpost.objects.create(
                title=request.POST.get('title'), 
                author=request.POST.get('author'), 
                description=request.POST.get('description'),
                text=request.POST.get('text'),
            )
            new_post.save()
            context = {
                'message': 'The post has been created successfully.',
                'type': 'success'
            }
        except:
            context = {
                'message': 'Error creating post.',
                'type': 'danger'
            } 


    else: 
        context = {}
    return render(request, 'post/new_post.html', context)


