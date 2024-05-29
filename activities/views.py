from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import TrainingSession, Category


class TrainingSessionListView(ListView):
    model = TrainingSession
    template_name = 'index.html'
    paginate_by = 6
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.GET.get('category', None)
        if category_name:
            category = get_object_or_404(Category, name=category_name)
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
