from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateBlogForm

# Create your views here.

from applications.blog_app.models import blog_post


def HomeView(request):
    if request.method == "GET":
        model = blog_post
        blogs = model.objects.all()
        context_obj = {
            "blogs": blogs
        }
        template_name = "blog_app/index.html"
        return render(request, template_name=template_name, context=context_obj)


def BlogDetailView(request, blog_id):
    if request.method == "GET":
        model = blog_post
        detailed_blog = model.objects.get(pk=blog_id)
        context_obj = {
            "detailed_blog": detailed_blog
        }
        template_name = "blog_app/blog_detail.html"
        return render(request, template_name=template_name, context=context_obj)


def BlogCreateView(request):
    template_name = 'blog_app/create_blog.html'
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)
        print("++", form.__dict__)
        form.instance.author = request.user
        if form.is_valid():
            print("+++")
            form.save()
        print("++",form.errors)
        return HttpResponse('hello world')
    else:
        form = CreateBlogForm()
    return render(request, template_name, {"form": form})