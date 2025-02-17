from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(),name='login'),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
