from django.shortcuts import render
from django.http import HttpResponse

from .models import Exp



def index(request):
    latest_exp_list = Exp.objects.order_by('date')[:5]
    context = {
        'latest_exp_list': latest_exp_list,
    }
    return render(request, 'log/index.html', context)
