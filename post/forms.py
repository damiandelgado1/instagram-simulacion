from .models import Post
from django import forms

class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'image',
            'text'
        ]