from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        form = LoginForm()

    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')


@method_decorator
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email',)
    template_name = 'my_account.html'
    success_url = reverse_lazy('Applicants')


def get_object(self):
    return self.request.user
