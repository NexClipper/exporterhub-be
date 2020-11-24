from django.urls import path
from .views import MainView, RepositoryView

urlpatterns = [
    path('', MainView.as_view()),
    path('exporter', RepositoryView.as_view()),
]
