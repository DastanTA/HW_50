from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import UserCreationForm


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_tracker:project_main')
    else:
        form = UserCreationForm()
    return render(request, 'registration/user_create.html', context={'form': form})
