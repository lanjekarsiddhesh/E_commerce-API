from rest_framework import serializers
from productApp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            id : {'read_only':True}
        }