from django import forms
from django.forms import widgets
from task_tracker.models import Task


class TaskForm(forms.ModelForm):
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
