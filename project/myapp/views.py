from django.shortcuts import render, redirect
import django.contrib.auth.urls
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, TripForm, ProfileForm
from .models import Trip, Profile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
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

def more_info(request, id):
    trip = Trip.objects.get(id=id)
    user_trips = request.user.profile.trips.all()
    allow_join = True
    context = {'trip':trip, 'allow_join':allow_join}
    try:
        utrip = user_trips.get(id=id)
    except Trip.DoesNotExist:
        utrip = None
    if utrip != None:
        allow_join = False
        context = {'trip':trip,
        'allow_join':allow_join,
        'room_name_json':mark_safe(json.dumps(id))}
        return render(request, 'tripnum.html', context)
    return render(request, 'tripnum.html', context)

@login_required
def join_trip(request, id):
    trip_list = Trip.objects.all()
    for t in trip_list:
        if id == t.id:
            trip = t
            profile = request.user.profile
            profile.trips.add(trip)
            profile.trips_total = profile.trips_total + 1
            trip.num_people = trip.num_people + 1
            profile.save()
            trip.save()
    context = {'trip_list':trip_list}
    return render(request, 'trips.html', context)

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
def view_profile(request):
    profile = request.user.profile
    trip_list = profile.trips.all()
    context = {'profile':profile, 'trip_list':trip_list}
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        profile = request.user.profile
        if form.is_valid():
            profile.city = form.cleaned_data['city']
            profile.state = form.cleaned_data['state']
            profile.country = form.cleaned_data['country']
            profile.save()
            return redirect('/profile/')
    else:
        profile = request.user.profile
        data = {'city':profile.city,
            'state':profile.state,
            'country':profile.country}
        form = ProfileForm(data)
        context = {'form':form, 'profile':profile}
        return render(request, 'edit_profile.html', context)
