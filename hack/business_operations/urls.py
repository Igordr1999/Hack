from django.urls import path

from . import views

urlpatterns = [
    path("api/getCities/", views.GetCities.as_view()),
    path("api/getStories/", views.GetStories.as_view()),
    path("api/getGuide/", views.GuideView.as_view()),
    path("api/getRoute/", views.RouteDetailView.as_view()),
    path("api/getRouteList/", views.RouteListView.as_view()),
    path("api/createRoute/", views.RouteCreate.as_view()),
]
