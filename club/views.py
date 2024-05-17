from django.shortcuts import render
# from django.views import generic
from .models import TrainingSession


def training_sessions_list(request):
    sessions = TrainingSession.objects.all()
    return render(request, 'training_sessions_list.html', {'sessions': sessions})
