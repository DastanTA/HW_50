from django import forms
from django.forms import widgets
from task_tracker.models import Type, Status, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']
        widgets = {'description': widgets.Textarea(attrs={"cols": 24, "rows": 3}),
                   'types': widgets.CheckboxSelectMultiple}
