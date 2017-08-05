from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Work_Logs, Social_Blogs, Technology_Blogs


# Home page for the Blogs
def index_blogs(request):
    work_logs = Work_Logs.objects.all()
    social_blogs = Social_Blogs.objects.all()
    tech_blogs = Technology_Blogs.objects.all()
    template =loader.get_template('blogs/index_blogs.html')
    # This is the information that the html template needs
    context = {
        'work_logs': work_logs,
        'social_blogs': social_blogs,
        'tech_blogs': tech_blogs,

    }
    return HttpResponse(template.render(context, request))

# View a person blog
def view_blogs(request, title):
    return HttpResponse("<p> hello</p>")

# View a person blog
def create_blogs(request):
    return HttpResponse("<p> hello</p>")


# View a person blog
def manage_blogs(request):
    return HttpResponse("<p> hello</p>")
