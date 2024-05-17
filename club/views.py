from django.shortcuts import render
from django.views import generic
from .models import TrainingSession


# Create your views here.
class TrainingSessionList(generic.ListView):
    queryset = TrainingSession.objects.all()
    template_name = "training_list.html"
