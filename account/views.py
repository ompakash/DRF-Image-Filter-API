import uuid
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.contrib.auth import login,  logout, authenticate

from django.contrib.auth.models import User
from account.serializer import RegisterSerializer
from django.conf import settings
from django.core.mail import send_mail



def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return True if re.fullmatch(regex, email) else False

class RegitsterView(APIView):

    def post(self, request):
        data = request.data
        if not (validate_email(data['username'])):
            return Response({'status':status.HTTP_406_NOT_ACCEPTABLE,'errors':"Invalid email!",'msg':"Something went wrong!"})

        user_qrysets = User.objects.filter(username=data['username'])
        if user_qrysets.count() > 0:
            return Response({'status':status.HTTP_406_NOT_ACCEPTABLE,'errors':"User already exists!",'msg':"Something went wrong!"})

        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED, 'data': serializer.data, 'message': 'Your account has been created.'})

        return Response({'status': status.HTTP_403_FORBIDDEN, 'error': serializer.errors, 'message': 'Something went wrong!'})


# class LogoutView(APIView):
#     permission_classes  = [IsAuthenticated]
#     def get(self, request):
#         logout(request)
#         return Response({'status': status.HTTP_200_OK, 'data': "Success", 'message': 'User Logged out successfully'})


class ForgetPasswordView(APIView):

    def get(self, request):
        token = request.GET['token']
        print(token)
        password = request.data["password"]

        user = User.objects.get(email=token)
        user.set_password(password)
        user.save()

        return Response({'status': status.HTTP_201_CREATED, 'data': "Success", 'message': 'Password recovered successfully.'})
            

    def post(self, request):
        data = request.data
        email = request.data['username']

        if not (validate_email(data['username'])):
            return Response({'status':status.HTTP_406_NOT_ACCEPTABLE,'errors':"Invalid email!",'msg':"Something went wrong!"})

        user_qrysets = User.objects.filter(username=data['username'])
        if user_qrysets.count() < 1:
            return Response({'status':status.HTTP_406_NOT_ACCEPTABLE,'errors':"User does not exists!",'msg':"Please create a account."})

        token = uuid.uuid1()

        user = user_qrysets[0]
        user.email = token
        user.save()

        subject = 'Forgot Password'
        message = f'Hi {email}, you requested for forgot password.. \n Click on link: http://127.0.0.1:8000/account/forgotpassword/?token={token}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email, ]

        send_mail(subject, message, from_email, recipient_list)

        return Response({'status': status.HTTP_201_CREATED, 'data': "serializer.data", 'message': 'Email sent.'})
