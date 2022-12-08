from django.core.paginator import Paginator
from django.views.generic import DetailView, CreateView
from django.db.models import Q
from task_tracker.models import Project
from task_tracker.forms import ProjectForm
from task_tracker.views.base_views import SearchView


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
    tasks_paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.object.tasks.all()
        paginator = Paginator(tasks, self.tasks_paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        context['tasks'] = page_obj.object_list
        return context


class ProjectCreate(CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    form_class = ProjectForm
