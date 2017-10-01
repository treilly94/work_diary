from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserForm, UserSettingsForm, UserSettingsExtendedForm
from log.models import WorkLog
from .models import Account
import datetime

def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

# Home page for the Blogs
# class HomeView(generic.ListView):
#     template_name = 'home/home_index.html'
#     context_object_name = 'all_blogs'
#
#     def get_queryset(self):
#         if not self.request.user.is_authenticated():
#             return render(self.request, 'home/login.html')
#         else:
#             return WorkLog.objects.order_by('-creation_date')[:3]

def HomeView(request):
    logs =  WorkLog
    template_name = 'home/home_index.html'
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        recent_logs = logs.objects.order_by('-creation_date')[:3]
        return render(request, template_name, {'all_blogs' : recent_logs})


def registration(request):
        form = UserForm(request.POST or None)
        if form.is_valid():
            # creates an object from the form but doesn't save it to the database yet
            user = form.save(commit=False)
            #clean (nomrlaized) data, data that is formatting properly
            firstname=form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            increment=0
            username=None
            user_check = lastname[0:5] + firstname[:1]
            while username is None:
                try:
                    User.objects.get(username=user_check)
                    user_check = lastname[0:5] + firstname[:1] + str(increment)
                except Exception:
                    username = user_check

            user.username =  username
            user.set_password(password)
            user.save()

            #returns User Objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:create_account')

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


def AccountView(request):
    model = Account
    template_name = 'home/view_account.html'
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')
    else:
        account = model.objects.get(user=request.user)
        return render(request, template_name, {'account': account})

# class UpdateAccountView(UpdateView):
#     model=Account
#     fields=['user', 'date_of_birth', 'location']
#     template_name_suffix = '_update_form'


class CreateAccountView(CreateView):
    model = Account
    fields =['user','date_of_birth','location']



def UpdateAccountView(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')

    user = request.user
    account = Account.objects.get(user=user)

    if request.method == 'POST':
        #create the form instance and populate with data
        form_user = UserSettingsForm(request.POST)
        form_extended = UserSettingsExtendedForm(request.POST)

        # Check if form is valid
        if form_user.is_valid() and form_extended.is_valid():
            # Save the User models fields
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            # Save the Account models fields
            account.location = request.POST['location']
            account.date_of_birth = request.POST['date_of_birth']
            account.modified_date = datetime.datetime.today()
            account.save()

            return redirect('home:view_account')
    else:
        form_user = UserSettingsForm(instance=user)
        form_extended = UserSettingsExtendedForm(instance=account)

    return render(request, 'home/account_update.html', {'form_user': form_user, 'form_extended': form_extended})

def DeactivateAccount(request):
    if not request.user.is_authenticated():
        return render(request, 'home/login.html')

    user = request.user
    if request.method == 'POST':
        user.is_active == False
        return redirect('home:login_user')

    return render(request, 'home/user_confirm_delete.html')