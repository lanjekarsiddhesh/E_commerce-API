from rest_framework import serializers
from productApp.models import *
from userApp.models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            id : {'read_only':True}
        }

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategory
        fields = ['id','name','Category_id']
        extra_kwargs = {
            id : {'read_only':True}
        }

class CategorySerializer(serializers.ModelSerializer):
    SubCategory = SubCategorySerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ['id','name','SubCategory']
        extra_kwargs = {
            id : {'read_only':True}
        }

class CompanySerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Company
        fields = ['id','name','product']
        extra_kwargs = {
            id : {'read_only':True}
        }

# User serializer

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=8,style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = Myuser
        fields = ['id','full_name','email','password','password2']
        extra_kwargs = {
            'password': {'write_only': True}
            }
        
    def validate(self,attr):
        password = attr.get('password')
        password2 = attr.get('password2')
        if password != password2:
            raise serializers.ValidationError("Password must match")
        return attr
        
    def create(self, validated_data):
        return Myuser.objects.create_user(**validated_data)
        # return user.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    class Meta:
        model = Myuser
        fields = ['email','password']