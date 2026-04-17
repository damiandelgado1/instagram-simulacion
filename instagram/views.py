from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class LoginView(TemplateView):
    template_name = "login.html"


class RegisterView(TemplateView):
    template_view = "register.html"


class LegalView(TemplateView):
    template_view = "legal.html"


class ContactView(TemplateView):
    template_view = "contact.html"