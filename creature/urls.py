from . import views
from django.urls import path

urlpatterns = [
    path('', views.AnimalList.as_view(), name='home'),
]