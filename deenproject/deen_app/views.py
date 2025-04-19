from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.

def home(request):
  return render(request, 'deen_app/home/index.html')

def about(request):
  return render(request, 'deen_app/home/about.html')

def dashboard(request):
  return render(request, 'deen_app/home/dashboard.html')
