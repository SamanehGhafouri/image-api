from django.shortcuts import render
from rest_framework import generics

from .models import UploadImage
from .serializers import UploadImageSerializer


class CreateImageView(generics.CreateAPIView):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer

    # def perform_create(self, serializer):
    #     serializer.save()


class ListImageView(generics.ListAPIView):
    queryset = UploadImage.objects.all()
    serializer_class = UploadImageSerializer
