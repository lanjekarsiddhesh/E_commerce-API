from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from productApp.models import *
from .serilaizer import *

# Create your views here.
class ProductAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk:
            productData = Product.objects.get(id=pk)
            productSerializer = ProductSerializer(productData)
        else:
            productData = Product.objects.all()
            productSerializer = ProductSerializer(productData,many=True)
        return Response(productSerializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        productSerializer = ProductSerializer(data=request.data)
        if productSerializer.is_valid():
            productSerializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        else:
            return Response(productSerializer.errors,status=status.HTTP_400_BAD_REQUEST)