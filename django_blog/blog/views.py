from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def home(request):
  return render(request, "blog/home.html")


def register(request):
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user) #auto login after registration
      return redirect("home")
    

  else:
    form = CustomUserCreationForm()  

  return render(request, "blog/register.html", {"form": form})  

@login_required
def profile(request):
  if request.method == "POST":
    request.user.email = request.POST.get("email")
    request.user.save()
    return redirect("profile")
  
  return render(request, "blog/profile.html")