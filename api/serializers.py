from rest_framework import serializers
from .models import ImageFilter

class ImageFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFilter
        fields = '__all__'
