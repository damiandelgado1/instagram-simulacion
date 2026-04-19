from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegistrationForm
from profiles.models import User


class HomeView(TemplateView):
    template_name = "templates/general/home.html"


class LoginView(TemplateView):
    template_name = "templates/general/login.html"


class RegisterView(CreateView):
    template_view = "templates/general/register.html"
    model = User
    success_url = reverse_lazy("home")
    form_class = RegistrationForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, "Hello World.")
        return super(RegisterView, self).form_valid(form)


class LegalView(TemplateView):
    template_view = "templates/general/legal.html"


class ContactView(TemplateView):
    template_view = "templates/general/contact.html"