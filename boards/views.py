from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializer
from rest_framework import viewsets
# Create your views here.

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer