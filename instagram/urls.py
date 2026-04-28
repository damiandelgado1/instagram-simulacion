from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, RegisterView, LoginView, ContactView, LegalView, logout_view, ProfileDetailView, ProfileUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('profile/', ProfileDetailView.as_view(), name="profile_detail"),
    path('profile/update/<pk>/', ProfileUpdateView.as_view(), name="profile_update"),
    path('legal/', LegalView.as_view(), name="legal"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)