from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Exp



class IndexView(generic.ListView):
    template_name = 'log/index.html'
    context_object_name = 'latest_exp_list'

    def get_queryset(self):
        """
        Return the all Exp alphabetically
        """
        return Exp.objects.order_by('date')

def tom(request):
    latest_exp_list = Exp.objects.order_by('date')[:5]
    context = {
        'latest_exp_list': latest_exp_list,
    }
    return render(request, 'log/tom.html', context)

def base(request):
    return render(request, 'log/base.html')
