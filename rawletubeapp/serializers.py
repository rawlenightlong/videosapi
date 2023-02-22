from .models import Video
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Video Serializer
class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'link']
