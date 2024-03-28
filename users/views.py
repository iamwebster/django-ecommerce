from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


from .forms import UserLoginForm, UserRegistrationForm, ProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                # messages.success(request, f'{username} successfully log in.')

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
        
    return render(request, 'users/login.html', {'form': form})


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserRegistrationForm(instance=request.user)

    return render(request, 'users/update_profile.html', {'form': form})


def user_cart(request):
    return render(request, 'users/cart_page.html')