from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimalList.as_view(), name='home'),
]