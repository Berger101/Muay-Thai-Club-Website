from django.contrib import admin
from .models import TrainingSession, Booking
from django_summernote.admin import SummernoteModelAdmin


class TrainingSessionAdmin(SummernoteModelAdmin):

    summernote_fields = ('description',)
    list_display = ('instructor', 'date', 'time')
    # search_fields = ['instructor']
    # list_filter = ('status',)
    # prepopulated_fields = {'slug': ('instructor',)}


admin.site.register(TrainingSession, TrainingSessionAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')


admin.site.register(Booking, BookingAdmin)
