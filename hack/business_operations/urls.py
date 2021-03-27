from django.urls import path

from . import views

urlpatterns = [
    path("api/getCities/", views.GetCities.as_view()),
    path("api/getStories/", views.GetStories.as_view()),
    path("api/getGuide/", views.GuideView.as_view()),
]
