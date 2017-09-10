from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.views import generic
from .forms import UserForm



def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def HomeView(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        return render(request, 'home/home_index.html')


def registration(request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            # creates an object from the form but doesn't save it to the database yet
            user = form.save(commit=False)
            #clean (nomrlaized) data, data that is formatting properly
            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User Objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')

        return render(request, 'home/registration.html', {'form': form})

def login_user(request):
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
                else:
                    return render(request, 'home/login.html', {'error_message': 'Your account has been disabled'})
            else:
                return render(request, 'home/login.html', {'error_message': 'Invalid login'})
        return render(request, 'home/login.html')



def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'home/login.html', context)

