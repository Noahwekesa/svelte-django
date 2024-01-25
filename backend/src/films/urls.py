from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('films', views.FilmViewSet, basename='films')
urlpatterns = router.urls

'''
urlpatterns = [
    path('films/', views.FilmListAPIView.as_view()),  # api/films
    path('films/<int:pk>/', views.FilmDetailAPIView.as_view()),  # api/films
]
'''
