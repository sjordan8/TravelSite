from django.shortcuts import render, redirect
import django.contrib.auth.urls
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, TripForm
from .models import Trip, Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json


# Create your views here.
def index(request):
    trip_list = Trip.objects.all()
    trip = trip_list[0]
    context = {'trip':trip}
    return render(request, 'index.html', context)

@csrf_exempt
def trips(request):
    trip_list = Trip.objects.all()
    context = {'trip_list':trip_list}
    return render(request, 'trips.html', context)

# @login_required
# def join_trip(request):
#     request.trip

@csrf_exempt
def new_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            t = Trip(
            name = form.cleaned_data['name'],
            description = form.cleaned_data['description'],
            start_date = form.cleaned_data['start_date'],
            end_date = form.cleaned_data['end_date'],
            author = request.user,
            image = form.cleaned_data['image'],
            image_description = form.cleaned_data['image_description'])
            t.save()
            return redirect('/trips/')
    else:
        form = TripForm()
        context = {'form':form}
        return render(request, 'new_trip.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            profile = Profile()
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'registration/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    profiles = Profile.objects.all()
    for i in profiles:
        if i.user.id == request.user.id:
            context = {'profile':i}
            return render(request, 'profile.html', context)
        else:
            return render(request, 'profile.html')
    return render(request, 'profile.html')
