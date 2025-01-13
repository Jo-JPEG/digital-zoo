from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "hungry"), (1, "full"))

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="animal_posts")
    type = models.CharField(max_length=100)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_fed = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    danger = models.IntegerField(default=0)