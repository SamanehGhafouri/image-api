from dataclasses import field
import imp
from rest_framework import serializers
from .models import UploadImage


class UploadImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImage
        fields = ['id', 'name', 'image',]