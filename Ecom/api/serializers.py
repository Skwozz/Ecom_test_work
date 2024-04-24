from django.http import request
from rest_framework import serializers
from .permissions import IsAdminOrReadOnly
from rest_framework.serializers import ModelSerializer
from .models import User, Stock, Category, Equipment

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class CategorySerializer(ModelSerializer):
     class Meta:
         model = Category
         fields = '__all__'


class EquipmentSerializer(ModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
         model = Equipment
         fields = '__all__'



