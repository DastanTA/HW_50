from django import forms
from django.forms import widgets
from task_tracker.models import Type, Status, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'types']
        widgets = {'description': widgets.Textarea(attrs={"cols": 24, "rows": 3}),
                   'types': widgets.CheckboxSelectMultiple}


# class TaskForm(forms.Form):
#     summary = forms.CharField(max_length=40, required=True, label='заголовок')
#     description = forms.CharField(
#         max_length=500, required=False,
#         label='описание', widget=forms.Textarea(attrs={"cols": 24, "rows": 3}))
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), label='статус')
#     types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), label='types',
#                                            widget=forms.CheckboxSelectMultiple)
