from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from task_tracker.models import Project
from task_tracker.forms import ProjectForm
from task_tracker.views.base_views import SearchView


class ProjectMainPage(SearchView):
    template_name = 'projects/project_index.html'
    context_object_name = 'projects'
    paginate_by = 4
    paginate_orphans = 1
    queryset = Project.objects.filter(is_deleted=False).order_by('start_date')

    def get_query(self):
        query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
        return query


class ProjectView(DetailView):
    template_name = 'projects/project.html'
    queryset = Project.objects.filter(is_deleted=False)
    tasks_paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.object.tasks.filter(is_deleted=False)
        paginator = Paginator(tasks, self.tasks_paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        context['tasks'] = page_obj.object_list
        return context


class ProjectCreate(LoginRequiredMixin, CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    form_class = ProjectForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect('accounts:login')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('view_project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    context_object_name = 'project'
    success_url = reverse_lazy('task_tracker:project_main')

    def form_valid(self, form):
        success_url = self.get_success_url()
        print(success_url)
        self.object.is_deleted = True
        self.object.save()
        return redirect(success_url)

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.is_deleted = True
    #     self.object.save()
    #     return redirect(success_url)