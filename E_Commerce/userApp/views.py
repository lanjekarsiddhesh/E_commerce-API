# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from .models import *
# from .serilazier import *
# from rest_framework.permissions import IsAdminUser, IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth import authenticate



# # Create your views here.
# def get_token(user):
#     refresh = RefreshToken.for_user(user)
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#     }

# class RegistrationView(APIView):
#     renderer_classes = [customRenderers]
#     def post(self, request, format=None):
#         serializer = RegistrationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user_ = serializer.save()
#         token = get_token(user_)
#         return Response({"MSG":"Given user data is created.","token":token},status=status.HTTP_201_CREATED)
        
#     def get(self,request,format=None):
#         userData = Myuser.objects.all()
#         serializer = RegistrationSerializer(userData,many=True)
#         return Response(serializer.data,status=status.HTTP_302_FOUND)


# class Login(APIView):
#     renderer_classes = [customRenderers]
#     def post(self,request,format=None):
#         seri_data = LoginSerializer(data=request.data)
#         if seri_data.is_valid(raise_exception=True):
#             email = request.data['email']
#             password = request.data['password']
#             usr = authenticate(email=email,password=password)
#             if usr is not None :
#                 token = get_token(usr)
#                 return Response({'msg':"Login successfully","token":token},status=status.HTTP_202_ACCEPTED)
#             else:
#                 return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
            
