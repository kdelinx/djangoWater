# coding: utf-8
from django.shortcuts import (render, get_object_or_404,
                              HttpResponseRedirect, Http404)
from django.core.urlresolvers import reverse
from users.models import User
from users.forms import UserEditForm, UserCreateForm
from django.contrib.auth import authenticate, login


def profile(request):
    user = get_object_or_404(User)
    context = {
        'profile': user,
    }
    return render(request, 'users/profile.html', context)


def edit(request):
    user = get_object_or_404(User, id=request.user.id)
    form = UserEditForm(instance=user)
    if request.POST:
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    context = {
        'form': form,
    }
    return render(request, 'users/edit.html', context)


def register(request, autologin=True):
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        if autologin:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = authenticate(username=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('user:profile'))
        else:
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'users/register.html', {'form': form})
