from django.shortcuts import render
from .models import Board
from .serializers import BoardSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.

class BoardViewSet(viewsets.ModelViewSet, APIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


    
