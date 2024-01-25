from django.shortcuts import render
from rest_framework import generics, viewsets
from films.models import Film

from films.serializers import FilmSerializer

# creating a set of api views to, create, update and delete objs


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


'''
class FilmListAPIView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class FilmDetailAPIView(generics.RetrieveAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    '''
