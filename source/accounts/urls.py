from django.contrib.auth.views import LoginView, LogoutView
# from accounts.views import logout_view, login_view
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]