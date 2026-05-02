from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView, FormView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from profiles.models import User
from django.contrib.auth import authenticate, login, logout
from profiles.models import Profile, Follow
from post.models import Post
from .forms import ProfileFollow
import ipdb



class HomeView(TemplateView):
    template_name = "general/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            follows = Follow.objects.filter(follower=self.request.user.profile).values_list('following__user', flat=True)
            last_posts = Post.objects.filter(user__profile__user__in = follows)

        else:
            last_posts = Post.objects.all().order_by('-created_at')[:5]
            context['last_posts'] = last_posts

            return context


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


@method_decorator(login_required, name="dispatch")
class ProfileListView(ListView):
    model = Profile
    templa_name = "general/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)


@method_decorator(login_required, name="dispatch")
class ProfileDetailView(DetailView, FormView):
    model = Profile
    template_view = "general/profile_detail.html"
    context_object_name = "profile"
    form_class = ProfileFollow

    def get_initial(self):
        self.initial['profile.pk'] = self.get_object().pk
        return super().get_initial()

    def form_valid(self, form):
        profile_pk = form.cleaned_data.get('profile_pk')
        action = form.cleaned_data.get('action')
        following = Profile.objects.get(pk=profile_pk)

        if Follow.objects.get_or_create(
            follower = self.request.user.profile,
            following = following
        ).exist():
            Follow.objects.filter(
                follower = self.request.user.profile,
                following = following
            ).delete()
        else:
            Follow.objects.get_or_create(
                follower = self.request.user.profile,
                following = following
            )

        if action == 'follow':
            Follow.objects.get_or_create(
                follower = self.request.user.profile,
                following = following
            ).exist()

        elif action == 'unfollow':
            Follow.objects.filter(follower=self.request.user.profile, following=following)
            messages.add_message(self.request, messages.SUCCESS, f"Se ha dejado de seguir")
            { following.user.username }

    def get_success_url(self):
        return reverse('profile_detail', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(UpdateView):
    model = Profile
    template_view = "general/profile_update.html"
    context_object_name = "profile"
    fields = ["user", "photo", "bio"]
    
    def dispatch(self, request, *args, **kwargs):
        user_profile = self.get_object()
        if user_profile.user != self.request.user:
            return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, "Perfil Editado")
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('profile_detail', args=[self.object.pk])


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'Se ha Cerrado la Sesion')
    return HttpResponseRedirect(reverse('home'))