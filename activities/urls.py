from . import views
from django.urls import path
from .views import TrainingSessionListView, TrainingSessionDetailView


#  urlpattern for TrainingSessionList class-based view (from activities/views.py) named home.
urlpatterns = [
    path('', TrainingSessionListView.as_view(), name='activities'),
    path('activities/<int:pk>/', TrainingSessionDetailView.as_view(), name='training_session_detail'),
    path('category/<str:category_name>/', views.TrainingSessionListView.as_view(), name='category_sessions'),
]
