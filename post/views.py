from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
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


@method_decorator(login_required, name="dispatch")
class PostDetailView(DetailView):
    template_name = "post/post_detail.html"
    model = Post
    context_object_name = "post"


@login_required
def like_post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.user in post.likes.all():
        messages.add_message(request, messages.INFO, f"Ya le das Like a la Publicacion")
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        messages.add_message(request, messages.INFO, "Like a la Publicacion")
        return HttpResponseRedirect(reverse('post_detail', args=[pk]))