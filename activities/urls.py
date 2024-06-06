from . import views
from django.urls import path
from .views import TrainingSessionListView, TrainingSessionDetailView, BookingListView


urlpatterns = [
    path('', TrainingSessionListView.as_view(), name='activities'),
    path('activities/<int:pk>/', TrainingSessionDetailView.as_view(), name='training_session_detail'),
    path('category/<slug:category_slug>/', TrainingSessionListView.as_view(), name='category_sessions'),
    # CRUD (create, read, delete) bookings
    path('bookings/', BookingListView.as_view(), name='booking_list'),
]
