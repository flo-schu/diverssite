from django.urls import path

from django.contrib.auth import views

app_name = 'users'


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='users/login.html'), name = 'login'),
]
