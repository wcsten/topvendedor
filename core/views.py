from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views.generic import FormView, View, CreateView, \
    UpdateView, TemplateView

from core.models import User, Customer


#class IndexView(TemplateView):
#    template_name = 'core/home.html'
#
#   def get(self, request, *args, **kwargs):
#        return redirect('new_customer')


class HomeView(TemplateView):
    template_name = 'core/home.html'
