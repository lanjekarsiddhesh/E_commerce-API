from djoser.serializers import UserCreateSerializer
from djoser.serializers import UserCreatePasswordRetypeSerializer
from userApp.models import Myuser as User

class MyUserCreationSerializer(UserCreatePasswordRetypeSerializer):
    class Meta():
        model = User
        fields = ['id','email','full_name','password']