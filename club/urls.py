from . import views
from django.urls import path


#  urlpattern for TrainingSessionList class-based view (from club/views.py) named home.
urlpatterns = [
    path('', views.TrainingSessionList.as_view(), name='home'),
]
