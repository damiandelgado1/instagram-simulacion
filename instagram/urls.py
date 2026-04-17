from django.contrib import admin
from django.urls import path
from .views import HomeView, RegisterView, LoginView, ContactView, LegalView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login/', RegisterView.as_view(), name="register"),
    path('register/', LoginView.as_view(), name="login"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('legal/', LegalView.as_view(), name="legal"),
    path('admin/', admin.site.urls),
]