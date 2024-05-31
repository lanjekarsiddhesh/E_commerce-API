# from rest_framework import serializers
# from .models import *
# from E_Commerce.utils import *

# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(min_length=8,style={'input_type': 'password'}, write_only=True)
#     class Meta:
#         model = Myuser
#         fields = ['id','full_name','email','password','password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#             }
        
#     def validate(self,attr):
#         password = attr.get('password')
#         password2 = attr.get('password2')
#         if password != password2:
#             raise serializers.ValidationError("Password must match")
#         return attr
        
#     def create(self, validated_data):
#         return Myuser.objects.create_user(**validated_data)
#         # return user.objects.create_user(**validated_data)

# class LoginSerializer(serializers.ModelSerializer):
#     email=serializers.EmailField()
#     class Meta:
#         model = Myuser
#         fields = ['email','password']

        