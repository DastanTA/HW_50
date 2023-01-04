from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import reverse, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from task_tracker.models import Project
from task_tracker.forms import ProjectForm, ProjectUserDeleteForm
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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'get_in.html')
        return super().dispatch(request, *args, **kwargs)


class ProjectView(PermissionRequiredMixin, DetailView):
    template_name = 'projects/project.html'
    queryset = Project.objects.filter(is_deleted=False)
    tasks_paginate_by = 3
    permission_required = 'task_tracker.view_project'
    permission_denied_message = "You don't have rights for this action!"

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


class ProjectCreate(PermissionRequiredMixin, CreateView):
    template_name = 'projects/create_project.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'task_tracker.add_project'
    permission_denied_message = "You don't have rights for this action!"

    def form_valid(self, form):
        project = form.save()
        project.users.add(self.request.user)
        return redirect('task_tracker:view_project', pk=project.pk)


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/update_project.html'
    form_class = ProjectForm
    context_object_name = 'project'
    queryset = Project.objects.filter(is_deleted=False)
    permission_required = 'task_tracker.change_project'
    permission_denied_message = "You don't have rights for this action!"

    def get_success_url(self):
        return reverse('task_tracker:view_project', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/delete_project.html'
    context_object_name = 'project'
    success_url = reverse_lazy('task_tracker:project_main')
    queryset = Project.objects.filter(is_deleted=False)
    permission_required = 'task_tracker.delete_project'
    permission_denied_message = "You don't have rights for this action!"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return redirect(success_url)


class DeleteUserFromProject(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'projects/update_users.html'
    form_class = ProjectUserDeleteForm
    context_object_name = 'project'
    queryset = Project.objects.filter(is_deleted=False)
    permission_required = 'task_tracker.can_change_users'
    permission_denied_message = "You don't have rights for this action!"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().users.all()

    def get_success_url(self):
        return reverse('task_tracker:view_project', kwargs={'pk': self.object.pk})
