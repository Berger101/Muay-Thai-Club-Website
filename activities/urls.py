from django.urls import path
from .views import (
    TrainingSessionListView, TrainingSessionDetailView,
    TrainingSessionCreateView, TrainingSessionUpdateView, TrainingSessionDeleteView
)


urlpatterns = [
    path('', TrainingSessionListView.as_view(), name='activities'),
    path('activities/<int:pk>/', TrainingSessionDetailView.as_view(), name='training_session_detail'),
    path('category/<slug:category_slug>/', TrainingSessionListView.as_view(), name='category_sessions'),
    # Bookings
    # path('bookings/', BookingListView.as_view(), name='booking_list'),
    # CRUD (create, read, delete) activities
    path('activities/new/', TrainingSessionCreateView.as_view(), name='training_session_create'),
    path('activities/<int:pk>/edit/', TrainingSessionUpdateView.as_view(), name='training_session_edit'),
    path('activities/<int:pk>/delete/', TrainingSessionDeleteView.as_view(), name='training_session_delete'),
]
