from django.shortcuts import render, get_object_or_404, redirect, reverse
from task_tracker.models import Task
from django.views.generic import View, TemplateView, FormView, ListView
from task_tracker.forms import TaskForm


class MainPage(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    paginate_by = 10
    paginate_orphans = 1

    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class CreateTask(FormView):
    template_name = 'create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view_task', kwargs={'pk': self.task.pk})


class UpdateTask(FormView):
    template_name = 'update.html'
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
        return render(request, 'delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('main')