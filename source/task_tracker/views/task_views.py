from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, TemplateView, FormView, CreateView
from django.db.models import Q
from task_tracker.models import Task, Project
from task_tracker.forms import TaskForm, ProjectTaskForm
from task_tracker.views.base_views import SearchView


class MainPage(SearchView):
    model = Task
    ordering = ['-created_at']
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    paginate_by = 10
    paginate_orphans = 1

    def get_query(self):
        query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value) | Q(project__title__icontains=self.search_value)
        return query


class TaskView(TemplateView):
    template_name = 'tasks/task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class CreateTask(CreateView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    model = Task


class ProjectTaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/project_task.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('view_project', pk=project.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        context['projectid'] = project.pk
        return context



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
