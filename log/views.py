from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import WorkLog


# Home page for the Blogs
class IndexBlogView(generic.ListView):
    template_name='log/index_blog.html'
    context_object_name ='all_blogs'
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return render(self.request, 'home/login.html')
        else:
            return WorkLog.objects.order_by('-creation_date')


# View a person blog
class DetailBlogView(generic.DetailView):
    model = WorkLog
    template_name = 'log/detail_blog.html'
    context_object_name = 'one_blog'


class BlogCreate(CreateView):
    model = WorkLog
    fields =['title','technology','type', 'description', 'link']