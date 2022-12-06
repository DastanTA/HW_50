from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import DetailView
from django.utils.http import urlencode
from django.db.models import Q
from task_tracker.models import Project, Task
from task_tracker.forms import ProjectForm
from task_tracker.base_views import SearchView


class ProjectMainPage(SearchView):
    model = Project
    ordering = ['start_date']
    template_name = 'projects/project_index.html'
    context_object_name = 'projects'
    paginate_by = 4
    paginate_orphans = 1

    def get_query(self):
        query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
        return query


class ProjectView(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.filter(project_id=self.kwargs.get('pk'))
        context['tasks'] = tasks
        return context
