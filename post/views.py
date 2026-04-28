from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from post.models import Post
from .forms import PostCreate


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    template_name = "post/post_create.html"
    form_class = PostCreate
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user

        messages.add_message(self.request, messages.SUCCESS, "Publicacion Creada")

        return super(PostCreateView, self).form_valid(form)