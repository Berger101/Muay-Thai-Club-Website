from . import views
from django.urls import path
from .views import TrainingSessionListView


#  urlpattern for TrainingSessionList class-based view (from club/views.py) named home.
urlpatterns = [
    path('activities/', TrainingSessionListView.as_view(), name='home'),
]
