from . import views
from django.urls import path


#  urlpattern for TrainingSessionList class-based view (from club/views.py) named training_sessions_list.
urlpatterns = [
    path('activities/', views.training_sessions_list, name='training_sessions_list'),
]
