from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from profiles.models import User
from django.contrib.auth import authenticate, login, logout
from profiles.models import Profile


class HomeView(TemplateView):
    template_name = "general/home.html"


class LoginView(FormView):
    template_name = "general/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=usuario, password=password)

        if user is not None:
            login(self.request, user)
            messages.add_message(self.request, messages.SUCCESS, f'Bienvenido de Nuevo {user.username}')
            return HttpResponseRedirect(reverse('home'))
        
        else:
            messages.add_message(
                self.request, messages.ERROR, 'Usuario o Contraseña No validos'
            )
            return super(LoginView, self).form_invalid(form)


class RegisterView(CreateView):
    template_view = "general/register.html"
    model = User
    success_url = reverse_lazy("home")
    form_class = RegistrationForm

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO, "Hello World.")
        return super(RegisterView, self).form_valid(form)


class LegalView(TemplateView):
    template_view = "general/legal.html"


class ContactView(TemplateView):
    template_view = "general/contact.html"


class ProfileDetailView(DetailView):
    model = Profile
    template_view = "general/profile_detail.html"
    context_object_name = "profile"


class ProfileUpdateView(UpdateView):
    model = Profile
    template_view = "general/profile_update.html"
    context_object_name = "profile"
    fields = ["user", "photo", "bio"]
    
    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil Editado")
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Se ha Cerrado la Sesion')
    return HttpResponseRedirect(reverse('home'))