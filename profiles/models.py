from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(verbose_name='Foto de Perfil', upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(verbose_name='Biografia', max_length=500, blank=True)
    birth_date = models.DateField(verbose_name='Fecha de Nacimiento', null=True, blank=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

    def __str__(self):
        return self.user

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="¿Quien sigue?", related_name='follower_set')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="¿A quien sigue?", related_name='following_set')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="¿Desde cuando lo Sigue?")

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower} follows {self.following}"

    class Meta:
        verbose_name = 'Seguidor'
        verbose_name_plural = 'Seguidores'