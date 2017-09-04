from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from home.forms import UserForm
from .models import Exp


# Home page for the Blogs
class IndexBlogBiew(generic.ListView):
    template_name='log/index_blog.html'
    context_object_name ='all_blogs'
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return render(request, 'log/login.html')
        else:
            return Exp.objects.order_by('-creation_date')

# View a person blog
class DetailBlogView(generic.DetailView):
    model = Exp
    template_name = 'log/detail_blog.html'
    context_object_name = 'one_blog'


class BlogCreate(CreateView):
    model = Exp
    fields =['author','title','technology','type', 'description', 'link']

class BlogUpdate(UpdateView):
    model = Exp
    fields = ['author', 'title', 'technology', 'type', 'description', 'link']


class BlogDelete(DeleteView):
    model = Exp
    success_url= reverse_lazy('blog:index_blog')