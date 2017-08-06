from django.shortcuts import render, get_object_or_404

from .models import Exp

# Home page for the Blogs
def index_blog(request):
    all_blogs = Exp.objects.order_by('-creation_date')
    return render(request, 'log/index_blog.html', {'all_blogs': all_blogs})

# View a person blog
def detail_blog(request, blog_id):
    view_blog = get_object_or_404(Exp, pk=blog_id)
    return render(request, 'log/detail.html', {'view_blog': view_blog})