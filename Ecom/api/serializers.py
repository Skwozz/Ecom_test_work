from django.http import request
from rest_framework import serializers
from .permissions import IsAdminOrReadOnly
from rest_framework.serializers import ModelSerializer
from .models import User, Stock, Category, Equipment

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']

class UserSerializer(ModelSerializer): # Сериализатор модели пользователя при помощи встроенного функционала rest_framework
    class Meta: # Определяем модель сериализатора
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data): # Регистрация пользователя через сериализатор
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class StockSerializer(ModelSerializer): # Сериализатор модели склада
    class Meta:
        model = Stock
        fields = '__all__'


class CategorySerializer(ModelSerializer): # Сериализатор модели категорий
     class Meta:
         model = Category
         fields = '__all__'


class EquipmentSerializer(ModelSerializer): # Сериализатор модели оборудования
    username = serializers.HiddenField(default=serializers.CurrentUserDefault()) # Скрываем поле username, используя
                                                                                 # при записи конкретного пользователя
    class Meta:
         model = Equipment
         fields = '__all__'



