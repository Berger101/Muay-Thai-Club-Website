from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import TrainingSession


class TrainingSessionListView(ListView):
    model = TrainingSession
    template_name = 'index.html'
    paginate_by = 6
    context_object_name = 'sessions'


class TrainingSessionDetailView(DetailView):
    model = TrainingSession
    template_name = 'training_session_detail.html'
    context_object_name = 'session'
