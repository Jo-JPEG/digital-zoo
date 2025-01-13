from django.contrib import admin
from .models import Animal
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Animal)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)

# Register your models here.
# admin.site.register(Animal)