# Generated by Django 5.0.4 on 2024-05-20 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_trainingsession_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='excerpt',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='trainingsession',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
    ]
