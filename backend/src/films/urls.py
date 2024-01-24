from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.FilmListAPIView.as_view()),  # api/films
    path('films/<int:pk>/', views.FilmDetailAPIView.as_view()),  # api/films
]
