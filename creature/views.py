from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Animal

# Create your views here.

class AnimalList(generic.ListView):
    queryset = Animal.objects.all()
    template_name = "animal/index.html"
    paginate_by = 6
