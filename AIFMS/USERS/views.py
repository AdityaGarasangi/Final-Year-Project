from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from .forms import UserBasicInfoForm, UserMoreInfoForm
from .serializers import UserSerailizer
from datetime import datetime


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Registration successful. You can now log in!")
            return redirect("login")  # Ensure 'login' URL is defined in your project
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        user_form = RegistrationForm()

    return render(request, "USERS/register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = AuthenticationForm()

    return render(request, "USERS/login.html", {"form": form})


def get_ip_address(request):
    user_ip_address = request.META.get("HTTP_X_FORWARDED_FOR")
    if user_ip_address:
        ip = user_ip_address.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserBasicInfoForm, UserMoreInfoForm


@login_required
def profile_page_view(request):
    user = request.user  # Using request.user, assuming user is authenticated
    basic_info_form = UserBasicInfoForm(request.POST or None, instance=user)
    more_info_form = UserMoreInfoForm(request.POST or None, instance=user.profile)

    if basic_info_form.is_valid() and more_info_form.is_valid():
        basic_info_form.save()
        more_info_form.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    # Handle invalid form submission (optional: add error messages)
    if request.method == "POST" and (
        not basic_info_form.is_valid() or not more_info_form.is_valid()
    ):
        messages.error(request, "There was an error with the form submission.")

    context = {
        "user": user,
        "user_ip": get_ip_address(request),
        "basic_info_form": basic_info_form,
        "more_info_form": more_info_form,
    }

    return render(request, "USERS/profile.html", context)


@login_required
def userSettings(request):
    user = User.objects.get(id=request.user.id)
    setting = user.profile

    seralizer = UserSerailizer(setting, many=False)

    return JsonResponse(seralizer.data, safe=False)


@login_required
def updateTheme(request):
    data = json.loads(request.body)
    theme = data["theme"]

    user = User.objects.get(id=request.user.id)
    user.profile.theme_value = theme
    user.profile.save()
    print("Request:", theme)
    return JsonResponse("Updated..", safe=False)


@method_decorator(login_required, name="dispatch")
class CustomLogoutView(View):
    def get(self, request):
        # Render the logout confirmation page
        return render(request, "USERS/logout.html")

    def post(self, request):
        # Log the user out and redirect
        logout(request)
        return redirect("login")  # Redirect to home page


@login_required
def edit_profile(request):
    user = request.user  # Get the currently logged-in user
    profile = user.profile  # Access the associated profile

    # Instantiate forms with current user data
    basic_info_form = UserBasicInfoForm(request.POST or None, instance=user)
    more_info_form = UserMoreInfoForm(request.POST or None, instance=profile)

    # Check if the forms are valid and save the data
    if request.method == "POST":
        if basic_info_form.is_valid() and more_info_form.is_valid():
            basic_info_form.save()  # Save changes to the user model
            more_info_form.save()  # Save changes to the profile model
            messages.success(request, "Profile updated successfully!")
            return redirect("profile")  # Redirect to the profile page

        # If form is invalid, show error messages
        else:
            messages.error(request, "Please fix the errors below.")

    context = {
        "basic_info_form": basic_info_form,
        "more_info_form": more_info_form,
    }

    return render(request, "USERS/edit_profile.html", context)
