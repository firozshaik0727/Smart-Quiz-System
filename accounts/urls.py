from django.urls import path
from .views import home, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(
            next_page='/'
        ),
        name='logout'
    ),
]