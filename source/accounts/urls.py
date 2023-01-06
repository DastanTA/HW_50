from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import RegisterView, UserDetailView, AllUsersView, UserChangeView


app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('all_users/', AllUsersView.as_view(), name='all_users'),
]
