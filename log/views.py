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

class tom(generic.DetailView):
    model = Exp
    template_name = 'log/tom.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Exp.objects


def base(request):
    return render(request, 'log/base.html')
