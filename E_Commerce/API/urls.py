from django.urls import path
from .views import *

urlpatterns = [
    path('Get-product/' , ProductAPI.as_view()),
    path('Get-product/<pk>' , ProductAPI.as_view()),
]
