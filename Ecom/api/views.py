from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Stock, Category, Equipment
from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer, StockSerializer, CategorySerializer, EquipmentSerializer
from rest_framework.decorators import api_view
from rest_framework.views import Response, APIView
from rest_framework import serializers
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    """Функция по выводу на главную страницу всех эндпоинтов API"""

    api_urls = [
        {'API Root': 'http://127.0.0.1:8000/api/'},
    {'endpoints for stock':
         ['http://127.0.0.1:8000/stock/',
          'http://127.0.0.1:8000/stock/create',
          'http://127.0.0.1:8000/stock/update/<str:pk>/',
          'http://127.0.0.1:8000/delete/stock/<str:pk>/',]},
        {'endpoints for user':
             ['http://127.0.0.1:8000/user/',
              'http://127.0.0.1:8000/user/create',
              'http://127.0.0.1:8000/user/update/<str:pk>/',
              'http://127.0.0.1:8000/delete/user/<str:pk>/', ]},
        {'endpoints for category':
             ['http://127.0.0.1:8000/category/',
              'http://127.0.0.1:8000/category/create',
              'http://127.0.0.1:8000/category/update/<str:pk>/',
              'http://127.0.0.1:8000/delete/category/<str:pk>/', ]},
        {'endpoints for equipment':
             ['http://127.0.0.1:8000/equipment/',
              'http://127.0.0.1:8000/equipment/create',
              'http://127.0.0.1:8000/equipment/update/<str:pk>/',
              'http://127.0.0.1:8000/delete/equipment/<str:pk>/', ]}

    ],
    return Response(api_urls)



"""Набор представлений методов для просмотра и создания"""
class UserViewSet(ModelViewSet): #
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)

class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAdminOrReadOnly,)

