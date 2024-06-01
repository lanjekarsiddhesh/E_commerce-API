from rest_framework import serializers
from productApp.models import *
from userApp.models import *

class CompanySerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Company
        fields = ['id','name']
        extra_kwargs = {
            id : {'read_only':True}
        }

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategory
        fields = ['name','Category_id']
        extra_kwargs = {
            id : {'read_only':True}
        }
    Category_id = serializers.StringRelatedField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
        extra_kwargs = {
            id : {'read_only':True}
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            id : {'read_only':True}
        }
    company = CompanySerializer()
    Category = serializers.StringRelatedField()
    subCategory = SubCategorySerializer()

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        extra_kwargs = {
            id : {'read_only':True},
            'user' : {'read_only':True}
        }

class CartItem(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'
    cart = CartSerializer()
    product = serializers.StringRelatedField()


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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','rating','review','user','Created_at']
    # user = ProductSerializer()
    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)