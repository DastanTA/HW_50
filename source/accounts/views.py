from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from accounts.forms import MyUserCreationForm
from accounts.models import Profile


class RegisterView(CreateView):
    model = User
    template_name = 'registration/user_create.html'
    form_class = MyUserCreationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next', None)
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('task_tracker:project_main')
        return next_url


class UserDetailView(PermissionRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0
    permission_required = 'accounts.can_view_all_users'

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object()

    def get_context_data(self, **kwargs):
        projects = self.object.projects.filter(is_deleted=False).order_by('-start_date')
        paginator = Paginator(projects, self.paginate_related_by, orphans=self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class AllUsersView(PermissionRequiredMixin, ListView):
    template_name = 'users.html'
    context_object_name = 'users'
    paginate_by = 6
    paginate_orphans = 1
    queryset = get_user_model().objects.all()
    permission_required = 'accounts.can_view_all_users'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'get_in.html')
        return super().dispatch(request, *args, **kwargs)