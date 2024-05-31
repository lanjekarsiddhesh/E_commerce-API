from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from productApp.models import *
from userApp.models import *
from .serilaizer import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import authenticate
from .renders import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .permissions import CustomPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import *


# Create your views here.
class CategoryAPI(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryAPI(ModelViewSet):
    queryset = subCategory.objects.all()
    serializer_class = SubCategorySerializer

class CompanyAPI(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ProductAPI(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CustomPermission]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = productFilters
    search_fields = ['name','description']
    ordering_fields = ['price']
  


# UserView
def get_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegistrationView(APIView):
    renderer_classes = [customRenderers]
    def post(self, request, format=None):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_ = serializer.save()
        token = get_token(user_)
        return Response({"MSG":"Given user data is created.","token":token},status=status.HTTP_201_CREATED)
        
    def get(self,request,format=None):
        userData = Myuser.objects.all()
        serializer = RegistrationSerializer(userData,many=True)
        return Response(serializer.data,status=status.HTTP_302_FOUND)


class Login(APIView):
    renderer_classes = [customRenderers]
    def post(self,request,format=None):
        seri_data = LoginSerializer(data=request.data)
        if seri_data.is_valid(raise_exception=True):
            email = request.data['email']
            password = request.data['password']
            usr = authenticate(email=email,password=password)
            if usr is not None :
                token = get_token(usr)
                return Response({'msg':"Login successfully","token":token},status=status.HTTP_202_ACCEPTED)
            else:
                return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_404_NOT_FOUND)
            
