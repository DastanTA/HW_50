from django import forms
from django.forms import widgets
from task_tracker.models import Task
from django.core.validators import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']
        widgets = {'description': widgets.Textarea(attrs={"cols": 24, "rows": 3}),
                   'types': widgets.CheckboxSelectMultiple}

    def clean_summary(self):
        banned_words = ['sex', 'bomb', 'kill', 'porn', 'секс', 'бомба', 'убью', 'порно']
        summary = self.cleaned_data.get('summary')
        summary_lst = summary.split()
        for word in summary_lst:
            if word in banned_words:
                raise ValidationError("Пожалуйста, не используйте запрещенные слова")
        return summary
