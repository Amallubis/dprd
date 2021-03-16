from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    catagories = Post.objects.values('catagory').distinct()
    context ={
        'title':'BLOG',
        'catagories':catagories,
        'subtitle':'BERITA TERKINI',
        'posts':posts
    }
    return render(request,'blog/index.html',context)


def catagory(request,catagoryInput):
    posts = Post.objects.filter(catagory=catagoryInput)
    catagories = Post.objects.values('catagory').distinct()
    context ={
        'title':'Berita',
        'catagories':catagories,
        'subtitle':'Berita',
        'posts':posts
    }
    return render(request,'blog/catagory.html',context)


def article_detail(request,slugInput):
    posts = Post.objects.get(slug=slugInput)
    catagories = Post.objects.values('catagory').distinct()
    context ={
        'title':'Berita',
        'catagories':catagories,
        'subtitle':'Berita',
        'posts':posts
    }
    return render(request,'blog/articleDetail.html',context)
    