# Generated by Django 4.2.17 on 2025-01-13 19:38

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creature', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
