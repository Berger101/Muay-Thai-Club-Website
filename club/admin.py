from django.contrib import admin
from .models import TrainingSession, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(TrainingSession)
class TrainingSessionAdmin(SummernoteModelAdmin):

    summernote_fields = ('description',)
    list_display = ('instructor', 'date', 'time')
    search_fields = ['instructor', 'description']
    list_filter = ('instructor', 'date')
    # prepopulated_fields = {}


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')


admin.site.register(Booking, BookingAdmin)
