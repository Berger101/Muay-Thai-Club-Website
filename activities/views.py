from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import TrainingSession, Category, Booking
# from .forms import BookingForm


class TrainingSessionListView(ListView):
    model = TrainingSession
    template_name = 'index.html'
    paginate_by = 8
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(categories=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class TrainingSessionDetailView(DetailView):
    model = TrainingSession
    template_name = 'training_session_detail.html'
    context_object_name = 'session'

    def post(self, request, *args, **kwargs):
        session = self.get_object()
        user = request.user

        if not user.is_authenticated:
            messages.error(
                request, "You need to log in to book or cancel a session.")
            return redirect('account_login')

        if 'book' in request.POST:
            # Handle booking creation
            booking, created = Booking.objects.get_or_create(
                session=session, user=user)
            if created:
                messages.success(
                    request, "You have successfully booked this session.")
            else:
                messages.info(request, "You have already booked this session.")
        elif 'cancel' in request.POST:
            # Handle booking cancellation
            Booking.objects.filter(session=session, user=user).delete()
            messages.success(request, "Your booking has been canceled.")

        return redirect('training_session_detail', pk=session.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['booking'] = Booking.objects.filter(
                session=self.object, user=self.request.user).first()
        else:
            context['booking'] = None
        return context


# class BookingListView(LoginRequiredMixin, ListView):
#     model = Booking
#     template_name = 'booking_list.html'
#     context_object_name = 'bookings'

#     def get_queryset(self):
#         return Booking.objects.filter(user=self.request.user)


# class BookingCreateView(LoginRequiredMixin, CreateView):
#     model = Booking
#     form_class = BookingForm
#     template_name = 'booking_form.html'
#     success_url = reverse_lazy('booking_list')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         form.instance.session = get_object_or_404(
#             TrainingSession, id=self.request.POST.get('session'))
#         return super().form_valid(form)


# class BookingDeleteView(LoginRequiredMixin, DeleteView):
#     model = Booking
#     template_name = 'booking_confirm_delete.html'
#     success_url = reverse_lazy('booking_list')

#     def get_queryset(self):
#         return Booking.objects.filter(user=self.request.user)


class TrainingSessionCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = TrainingSession
    template_name = 'training_session_form.html'
    fields = ['title', 'instructor', 'date', 'time', 'featured_image', 'categories', 'description', 'excerpt']
    success_url = reverse_lazy('activities')

    def test_func(self):
        return self.request.user.is_staff


class TrainingSessionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TrainingSession
    template_name = 'training_session_form.html'
    fields = ['title', 'instructor', 'date', 'time', 'featured_image', 'categories', 'description', 'excerpt']
    success_url = reverse_lazy('activities')

    def test_func(self):
        return self.request.user.is_staff


class TrainingSessionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TrainingSession
    template_name = 'training_session_confirm_delete.html'
    success_url = reverse_lazy('activities')

    def test_func(self):
        return self.request.user.is_staff
