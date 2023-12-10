from django.db import models
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from .forms import UserAddForm, UpdateUserForm
from django.views.generic import View, ListView
from django.contrib.auth.models import User




# Create your views here.
class UserCreationView(View):
    template_name = 'userApp/user_creation.html'
    
    def get(self, request):
        form=UserCreationForm
        user_add_form=UserAddForm

        return render(request, self.template_name, {'user_add_form':user_add_form, 'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        user_add_form = UserAddForm(request.POST)
        if form.is_valid() and user_add_form.is_valid():
            user= form.save()
            user_info=user_add_form.save(commit=False)
            user_info.user=user
            user_info.save()

            messages.success(request, 'User created')
            return redirect('UserApp:user-list')
        return render(request, self.template_name, {'user_add_form':user_add_form, 'form':form})


class UserListView(ListView):
    model = User
    template_name = 'userApp/user_list.html'
    context_object_name = 'users'




class UserUpdateView(View):
    template_name = 'userApp/user_update.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        update_form= UpdateUserForm(instance=user)
        form = UserAddForm(instance=user.user)
        return render(request, self.template_name, {'update_form':update_form, 'form':form})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        update_form = UpdateUserForm(request.POST, instance=user) #defalt model
        form = UserAddForm(request.POST, instance=user.user) #model
        if update_form.is_valid() and form.is_valid():
            user = update_form.save()
            form_user = form.save(commit=False)
            form_user.user=user
            form_user.save()
            messages.success(request, 'user updated')
            return redirect('UserApp:user-list')
        return render(request, self.template_name, {'update_form': update_form, 'form':form })







