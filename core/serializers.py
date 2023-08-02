from rest_framework.serializers import ModelSerializer
from .models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__' # return all the values in model
        fields = ['id', 'first_name', 'last_name', 'email', 'password']