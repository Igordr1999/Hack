from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("api/auth/", views.Auth.as_view()),
    path("api/refresh/", TokenRefreshView.as_view()),
    path("api/getUserInfo/", views.GetFullname.as_view()),
]
