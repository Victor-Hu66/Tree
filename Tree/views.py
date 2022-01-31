from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from .models import Button, Linktree
from .serializers import LinktreeSerializer, LinkbuttonsSerializer


def home (request):
    return HttpResponse("hello")

    
        
class LinktreeListView(generics.ListCreateAPIView):
    queryset = Linktree.objects.all()
    serializer_class = LinktreeSerializer

class LinkButtonListCreateView(generics.ListCreateAPIView):
    queryset = Button.objects.all()
    serializer_class = LinkbuttonsSerializer