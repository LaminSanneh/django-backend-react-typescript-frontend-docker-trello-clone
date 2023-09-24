from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardAPIListView.as_view(), name='board-list')
]
