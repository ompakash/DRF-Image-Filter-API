from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import ImageFilterSerializer
from .models import ImageFilter
from api.img_converter import ImgConverter
from rest_framework.permissions import IsAuthenticated

class ImageFilterViews(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, name=None):

        all_img = ImageFilter.objects.all()
        serializer = ImageFilterSerializer(all_img, many=True)

        return Response({'msg': 'all images', 'status': status.HTTP_200_OK, 'data': serializer.data})

    def post(self, request):
        serializer = ImageFilterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            process = request.data["process"]
            ImgConverter_obj = ImgConverter(process, serializer.data)
            output_address = ImgConverter_obj.callProcess()
                
            return Response({'msg': 'Done', 'status': status.HTTP_201_CREATED, 'payload': serializer.data, 'after_process': output_address})

        return Response({'msg': 'Something went wrong ', 'errors': "serializer.errors", 'status': status.HTTP_400_BAD_REQUEST})