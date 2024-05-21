from . import views
from django.urls import path
from .views import TrainingSessionListView, TrainingSessionDetailView


#  urlpattern for TrainingSessionList class-based view (from club/views.py) named home.
urlpatterns = [
    path('', TrainingSessionListView.as_view(), name='activities'),
    path('activities/<int:pk>/', TrainingSessionDetailView.as_view(), name='training_session_detail'),
]
