from django.shortcuts import render
from rest_framework import generics
from .models import Board
from .serializers import BoardListSerializer

class BoardAPIListView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardListSerializer
