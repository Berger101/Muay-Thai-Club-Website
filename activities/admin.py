from django.contrib import admin
from .models import TrainingSession, Category, Booking
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TrainingSession)
class TrainingSessionAdmin(SummernoteModelAdmin):

    summernote_fields = ('description',)
    list_display = ('title', 'instructor', 'date', 'time')
    search_fields = ['instructor', 'description']
    list_filter = ('title', 'instructor', 'date', 'categories')
    prepopulated_fields = {'title': ('instructor', 'date')}
    filter_horizontal = ('categories',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['categories'].queryset = Category.objects.filter(
            name__in=[Category.BOXING, Category.THAIBOXING, Category.BJJ,
                      Category.PRIVATETRAINING, Category.GROUPTRAINING, Category.EVENTS, Category.CORPORATEEVENTS, Category.KIDSCLASSES]
        )
        return form


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_title', 'session_date', 'session_time')

    def session_title(self, obj):
        return obj.session.title

    def session_date(self, obj):
        return obj.session.date

    def session_time(self, obj):
        return obj.session.time

    session_title.short_description = 'Session Title'
    session_date.short_description = 'Session Date'
    session_time.short_description = 'Session Time'
