from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, TemplateView, FormView, ListView, CreateView
from django.utils.http import urlencode
from django.db.models import Q
from task_tracker.models import Project
from task_tracker.forms import ProjectForm, SimpleSearchForm
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


