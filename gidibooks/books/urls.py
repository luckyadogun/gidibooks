from django.urls import path

from books import views

urlpatterns = [path("search/", views.search, name="search")]
