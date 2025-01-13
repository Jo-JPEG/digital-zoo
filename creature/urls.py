from django.urls import path
from . import views

urlpatterns = [
    path('', views.AnimalList.as_view(), name='home'),
    path('<slug:slug>/', views.animal_detail, name='animal_detail'),
]