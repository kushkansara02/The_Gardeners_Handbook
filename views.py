
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Customer, Flower

from .models import *
from .forms import *

# Create your views here.
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('userhome')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(user=user, username=user.username)
            WishList.objects.create(customer=customer, username=user.username)

            messages.success(request, 'Account was created successfully for ' + form.cleaned_data.get('first_name'))
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, "user_create.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('userhome')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('userhome')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'user_login.html', {})


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def userHome(request):
    return render(request, "home-page.html", {})


@login_required(login_url='login')
def myFamily(request):
    return render(request, "my-family.html", {})


@login_required(login_url='login')
def myGarden(request):

    username = request.user.username
    instance = WishList.objects.get(customer__username=username)

    form = WishListForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        #update wishlist

    flowers = Flower.objects.filter(customer__username=username)
    allFlowers = Flower.objects.all()
    wishList = Flower.objects.filter(wishlist__username=username)

    context = {
        'flowers': flowers,
        'allFlowers': allFlowers,
        'form': form,
        'wishlist': wishList
    }
    return render(request, "my-garden.html", context)


@login_required(login_url='login')
def weather(request):
    from .weatherAPI import Weather
    import requests, json
    weather = Weather("Brampton")

    today = weather.getWeatherToday()
    fiveday = weather.get5DayWeather()
    tips = ""

    if today[0] > 25 and "rain" not in today[5]:
        tips = "Make sure to give your plants some extra water today"

    elif today[0] <= 25 and "rain" not in today[5]:
        tips = "Today is a regular watering day for your plants"

    else:
        tips = "You don't need to water your plants today!"


    context = {
        "temperature": today[0],
        "feelslike": today[1],
        "forecast": fiveday,
        "description": today[5],
        "tips": tips
    }

    return render(request, "weather.html", context)


@login_required(login_url='login')
def myCalendar(request):
    return render(request, "my-calendar.html", {})


@login_required(login_url='login')
def sustainabilityTips(request):
    return render(request, "sustainability-tips.html", {})


@login_required(login_url='login')
def myMood(request):
    return render(request, "my-mood (1).html", {})
