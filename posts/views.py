from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        data = {
            'posts': posts
        }
        return render(request, 'layouts/main.html', context=data)


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {

        }

        return render(request, 'posts/posts.html', context=data)