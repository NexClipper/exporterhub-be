from django.urls import path
from .views import MainView, CategoryView, RepositoryView

urlpatterns = [
    path('', MainView.as_view()),
    path('category', CategoryView.as_view()),
    path('exporter', RepositoryView.as_view()),
]
