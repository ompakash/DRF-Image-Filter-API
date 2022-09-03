from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ImageFilterSerializer
from .models import ImageFilter
from api.img_converter import ImgConverter

ImgConverter_obj = ImgConverter()

class ImageFilterViews(APIView):
    def get(self,request,name = None):

        all_img = ImageFilter.objects.all()
        serializer = ImageFilterSerializer(all_img,many=True)

        return Response({'msg':'all images','status':status.HTTP_200_OK,'data':serializer.data})
        

    def post(self,request):
        serializer = ImageFilterSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            output_address = ImgConverter_obj.gray_scale(serializer.data['before_img'])
            return Response({'msg':'Done','status':status.HTTP_201_CREATED,'payload':serializer.data,'after_process': output_address})

        return Response({'msg':'Something went wrong ','errors':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})
