from django.shortcuts import render, redirect
import django.contrib.auth.urls
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, TripForm
from .models import Trip_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json


# Create your views here.
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def trips(request):
    trip_list = Trip_model.objects.all()
    context = {'trip_list':trip_list}
    return render(request, 'trips.html', context)

@csrf_exempt
def new_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            t = Trip_model(name=name,description=description,start_date=start_date,end_date=end_date,author=request.user)
            t.save()
            return redirect('/trips/')
    else:
        form = TripForm()
        context = {'form':form}
        return render(request, 'new_trip.html', context)
        # return Response(trip_dictionary)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('/')
@login_required
def profile(request):
    return render(request, 'profile.html')
