from django import forms
from django.contrib.auth import get_user_model
from django.forms import widgets
from task_tracker.models import Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types', 'project']
        widgets = {'description': widgets.Textarea(attrs={"cols": 24, "rows": 3, 'class': 'form-control'}),
                   'types': widgets.CheckboxSelectMultiple,
                   'summary': widgets.TextInput(attrs={'class': 'form-control'})}
        error_messages = {
            'summary': {'required': "Нельзя оставлять заголовок пустым!"},
            'description': {
                'required': "Пустым тоже нельзя оставлять описание!",
                'min_length': "Нельзя писать слишком короткое описание! Должно быть больше 20 символов"
            }
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'finish_date']
        widgets = {'description': widgets.Textarea(attrs={"cols": 24, "rows": 3, 'class': 'form-control'}),
                   'title': widgets.TextInput(attrs={'class': 'form-control'})}
        error_messages = {
            'title': {'required': "Нельзя оставлять название пустым!"},
            'description': {
                'required': "Пустым тоже нельзя оставлять описание!",
                'min_length': "Нельзя писать слишком короткое описание! Должно быть больше 10 символов"
            }
        }


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']
        widgets = {'description': widgets.Textarea(attrs={"cols": 24, "rows": 3, 'class': 'form-control'}),
                   'types': widgets.CheckboxSelectMultiple,
                   'summary': widgets.TextInput(attrs={'class': 'form-control'})}
        error_messages = {
            'summary': {'required': "Нельзя оставлять заголовок пустым!"},
            'description': {
                'required': "Пустым тоже нельзя оставлять описание!",
                'min_length': "Нельзя писать слишком короткое описание! Должно быть больше 20 символов"
            }
        }


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти",
                             widget=widgets.TextInput(attrs={
                                 'class': 'form-control me-2 ms-2',
                                 'type': 'search',
                                 'placeholder': 'найти', 'aria-label': 'search'}))


class ProjectUserDeleteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['users'].queryset = get_user_model().objects.exclude(pk=self.user.pk)

    class Meta:
        model = Project
        fields = ['users']
        widgets = {'users': widgets.CheckboxSelectMultiple}

    def save(self, commit=True):
        project = super().save(commit=commit)
        if commit:
            project.users.add(self.user)
            project.save()
        return project