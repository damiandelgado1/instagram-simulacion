from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def follow(request, user_to_follow_pk):
    user_2 = get_list_or_404(User, pk=user_to_follow_pk)

    if request.user != user_1:
        return HttpResponseForbidden()
    
    if user_1.profile.follows.filter(pk=user_2.pk).exists():
        return HttpResponseRedirect(reverse('profiles:profile', args=[user_2.username]))
    user_1.profile.follows.add(user_2.profile)