from django.views import generic

from .models import Exp



class IndexView(generic.ListView):
    template_name = 'log/index.html'
    context_object_name = 'latest_exp_list'

    def get_queryset(self):
        """
        Return the all Exp alphabetically
        """
        return Exp.objects.order_by('-date')

class UserView(generic.ListView):
    template_name = 'log/users.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        """
        Return the all Exp alphabetically
        """
        return Exp.objects.distinct('user').order_by('-user')

class BlogView(generic.ListView):
    template_name = 'log/blog.html'
    context_object_name = 'latest_exp_list'

    def get_queryset(self):
        """
        Return the all Exp alphabetically
        """
        return Exp.objects.order_by('-date')

class DetailView(generic.DetailView):
    model = Exp
    template_name = 'log/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Exp.objects


def base(request):
    return render(request, 'log/base.html')
	
class DetailView(generic.DetailView):
    model = Exp
    template_name = 'log/future.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Exp.objects
