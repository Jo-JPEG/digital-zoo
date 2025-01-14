from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Animal

# Create your views here.

class AnimalList(generic.ListView):
    queryset = Animal.objects.all()
    template_name = "animal/index.html"

def animal_detail(request, slug):
    """
    Display an individual :model:`creature.Animal`.

    **Context**

    ``post``
        An instance of :model:`creature...`.

    **Template:**

    :template:`blog/animal_detail.html`
    """

    queryset = Animal.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "creature/animal_detail.html",
        {"post": post},
    )
