from django.shortcuts import render
from .models import Article,Category,Post
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

# def show_index(request,*args , **kwargs):
    # print(args,kwargs)
    # print(request.user)
    # article_list=Article.objects.all()
    # category_list=Category.objects.all()
    # context={'article_list':article_list ,'category_list':category_list}

    # return render(request,'index.html')

# def contact_view(request,*args , **kwargs):
#     return HttpResponse('<h1>contact form</h1>')

    
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})


def index(request):
    context = {}
    return render(request, 'index.html', context)