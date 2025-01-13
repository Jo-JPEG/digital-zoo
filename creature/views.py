from django.shortcuts import render
from django.views import generic
from .models import Animal

# Create your views here.

class AnimalList(generic.ListView):
    model = Animal