from django.urls import path
from .views import chek_user, register, login_view, logout_view, register_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('chek-user', chek_user),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('register', register),
    path('custom-user', login_view),
    path('custom-logout', logout_view),
    path('custom-register', register_view)
]