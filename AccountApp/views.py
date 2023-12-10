from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from UserApp.forms import UpdateUserForm
from .models import AccountModel
from .forms import AccountInfoForm, AccountUpdateForm
from django.views.generic import View, ListView
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User

# Create your views here.
class AccountCreateView(View):
    template_name = 'accountApp/acc_create.html'

    def get(self, request):
        acc_crt_form = UserCreationForm #username, pass1, pass2
        acc_info_form = AccountInfoForm
        return render(request, self.template_name,{'acc_crt_form':acc_crt_form, 'acc_info_form':acc_info_form})


    def post(self, request):
        acc_crt_form = UserCreationForm(request.POST) #username, pass1, pass2
        acc_info_form = AccountInfoForm(request.POST) #user info
        if acc_crt_form.is_valid() and acc_info_form.is_valid():
            #save user acc
            user_create = acc_crt_form.save()
            #save user acc info
            user_info= acc_info_form.save(commit=False)
            #set user_create in user_info with (user) OneToOneField of AccountModel
            user_info.user = user_create
            user_info.save()

            messages.success(request, 'Account created successfull')
            return redirect('AccountApp:account-list')
        return render(request, self.template_name, {'acc_crt_form':acc_crt_form, 'acc_info_form':acc_info_form})


class AccountUpdateView(View):
    template_name = 'accountApp/acc_update.html'

    def get(self, request, pk):
        #user select by pk
        user = get_object_or_404(User, pk=pk)
        update_form = AccountUpdateForm(instance=user)
        acc_info = AccountInfoForm(instance=user.related_user)
        return render(request, self.template_name, {'acc_info':acc_info, 'update_form':update_form})


    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        #defalt model user info instance
        update_form = AccountUpdateForm(request.POST, instance=user) 
        acc_info = AccountInfoForm(request.POST, instance=user.related_user)
        if update_form.is_valid():
            user_update=update_form.save()
            acc_info_save = acc_info.save(commit=False)
            acc_info_save.user = user_update
            acc_info_save.save()
            messages.success(request, 'Account updated')
            return redirect('AccountApp:account-list')
        return render(request, self.template_name, {'update_form':update_form, 'acc_info':acc_info})


class AccountListView(ListView):
    model = User
    template_name = 'accountApp/account_list.html'
    context_object_name = 'accounts'
    queryset = User.objects.filter(is_superuser=False).prefetch_related('related_user')


def logout_view(request):
    logout(request)