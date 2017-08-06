from django.shortcuts import render, get_object_or_404
from .models import Exp

# Home page for the Blogs
def index_blogs(request):
    all_blogs = Exp.objects.order_by('-creation_date')
    return render(request, 'log/index.html', {'all_blogs': all_blogs})

# View a person blog
def view_blogs(request, pk):
    exp = get_object_or_404(Exp, pk=pk)
    return render(request, 'log/view_blogs.html', {'exp': exp})

# Favourite a blog
def favourite(request, log_id):
    logs = get_object_or_404(Exp, pk=log_id)


# View a person blog
def create_blogs(request):
    exp = Exp.objects.all()
    return render(request, 'log/index.html', {'exp': exp})


# View a person blog
def manage_blogs(request):
    exp = Exp.objects.all()
    return render(request, 'log/index.html', {'exp': exp})
