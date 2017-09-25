from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import WorkLog
from django.http import HttpResponseRedirect

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


class UpdateBlog(UpdateView):
    model=WorkLog
    fields=['title','technology','type', 'description', 'link']
    template_name_suffix = '_update_form'


class DeleteBlog(DeleteView):
    model=WorkLog
    success_url = reverse_lazy('blog:index_blog')
    template_name_suffix = '_confirm_delete'
