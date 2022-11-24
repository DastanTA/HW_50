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
        error_messages = {
            'summary': {'required': "Нельзя оставлять заголовок пустым!"},
            'description': {
                'required': "Пустым тоже нельзя оставлять описание!",
                'min_length': "Нельзя писать слишком короткое описание! Должно быть больше 20 символов"
            }
        }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('summary') == cleaned_data.get('description'):
            raise ValidationError('Заголовок и описание не должны быть идентичными!')
        return cleaned_data
