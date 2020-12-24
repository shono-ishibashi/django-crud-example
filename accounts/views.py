from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import UserCreateForm


class CreateAccount(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('study:list')

        return render(request, 'register.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'register.html', {'form': form})
