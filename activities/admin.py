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
            name__in=[Category.BOXING, Category.THAI_BOXING, Category.BJJ,
                      Category.PRIVATE_TRAINING, Category.GROUP_TRAINING, Category.EVENTS, Category.CORPORATE_EVENTS, Category.CHILDREN_CLASSES]
        )
        return form


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'session')


admin.site.register(Booking, BookingAdmin)
