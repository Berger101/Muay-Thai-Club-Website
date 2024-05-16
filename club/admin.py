from django.contrib import admin
from .models import TrainingSession, Booking


class TrainingSessionAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'date', 'time')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')


admin.site.register(TrainingSession, TrainingSessionAdmin)


admin.site.register(Booking, BookingAdmin)
