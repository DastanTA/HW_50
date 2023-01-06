from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not (first_name or last_name):
            raise forms.ValidationError('Надо заполнить имя или фамилию!')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {'first_name': 'имя', 'last_name': 'фамилия', 'email': 'E-mail'}


class ProfileChangeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'git_hub_profile', 'about']
