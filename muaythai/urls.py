from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("activities/", include("activities.urls"), name="activities-urls"),
    path("contact/", include("contact.urls"), name="contact-urls"),
    path('', include('club.urls'), name="club-urls"),
]
