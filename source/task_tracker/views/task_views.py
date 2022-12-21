from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
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

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False).filter(project__is_deleted=False)

    def get_query(self):
        query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value) | Q(project__title__icontains=self.search_value)
        return query



class TaskView(DetailView):
    template_name = 'tasks/task.html'
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False).filter(project__is_deleted=False)


class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        task = form.save()
        task.users.add(self.request.user)
        return redirect('task_tracker:view_task', pk=task.pk)


class ProjectTaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/project_task.html'
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        task.users.add(self.request.user)
        return redirect('task_tracker:view_project', pk=project.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        if project.is_deleted:
            raise Http404
        context['projectid'] = project.pk
        return context


class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = 'tasks/update.html'
    model = Task
    form_class = TaskForm
    context_object_name = 'task'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False).filter(project__is_deleted=False)

    def get_success_url(self):
        return reverse('task_tracker:view_task', kwargs={'pk': self.object.pk})


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('task_tracker:main')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_deleted=False).filter(project__is_deleted=False)

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.soft_delete()
        return HttpResponseRedirect(success_url)
