from django.shortcuts import render
from .models import Video
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import VideoSerializer


# Create your views here.


class VideoViewSet(viewsets.ModelViewSet):
    # Main query for this route
    queryset = Video.objects.all()
    #Serialzer for serializing output
    serializer_class = VideoSerializer
    #optional permission class set permission level
    permission_classes = [permissions.AllowAny]