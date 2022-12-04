from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, TemplateView, FormView, ListView
from django.utils.http import urlencode
from django.db.models import Q
from task_tracker.models import Task
from task_tracker.forms import TaskForm, SimpleSearchForm


class SearchView(ListView):

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.get_query()
        if self.search_value:
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get_query(self):
        query = Q(None)
        return query


class MainPage(SearchView):
    model = Task
    ordering = ['-created_at']
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    paginate_by = 10
    paginate_orphans = 1

    def get_query(self):
        query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
        return query


class TaskView(TemplateView):
    template_name = 'tasks/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class CreateTask(FormView):
    template_name = 'tasks/create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_task', kwargs={'pk': self.task.pk})


class UpdateTask(FormView):
    template_name = 'tasks/update.html'
    form_class = TaskForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_task', kwargs={'pk': self.task.pk})


class DeleteTask(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'tasks/delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('main')
