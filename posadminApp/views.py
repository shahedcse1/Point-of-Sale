from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import View



# Create your views here.

class HomeView(View):
    template_name='pos/index.html'

    def get(self, request):
        context = {
            'mess':'temp message'
        }
        return render(request, self.template_name, context)

