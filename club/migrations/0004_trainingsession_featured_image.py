# Generated by Django 5.0.4 on 2024-05-21 13:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_trainingsession_excerpt_trainingsession_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
