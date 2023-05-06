from django.urls import path
from .views import *

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('create/', MovieCreateView.as_view(), name='movie_create'),
    path('<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('<int:pk>/update/', MovieUpdateView.as_view(), name='movie_update'),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),
]