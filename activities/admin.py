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


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')


admin.site.register(Booking, BookingAdmin)
