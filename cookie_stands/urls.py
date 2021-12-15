from django.urls import path
from .views import CookiesDetails, CookiesList
urlpatterns =[
    path("all/",CookiesList.as_view(), name = "all" ),
    path('<int:pk>/',CookiesDetails.as_view(),name = "details"),
]