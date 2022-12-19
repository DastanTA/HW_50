from django import forms
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if not first_name or last_name:
            raise forms.ValidationError('Надо заполнить имя или фамилию!')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']



# class UserCreationForm(forms.ModelForm):
#     password = forms.CharField(label='пароль', strip=False, required=True, widget=forms.PasswordInput)
#     password_confirm = forms.CharField(label='подтверждение пароля', required=True,
#                                        widget=forms.PasswordInput, strip=False)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')
#         if password and password_confirm and password != password_confirm:
#             raise forms.ValidationError('Пароли не совпадают!')
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get('password'))
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']