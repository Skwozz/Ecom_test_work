from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Stock, Category, Equipment
from .serializers import UserSerializer, StockSerializer, CategorySerializer, EquipmentSerializer
from rest_framework.decorators import api_view
from rest_framework.views import Response, APIView
from rest_framework import serializers
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all': '/',
        'Search by Category': '/?category=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# @api_view(['GET'])
# def stockList(request):
#     items = Stock.objects.all()
#     serializer = StockSerializer(items, many=True)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def stockCreate(request):
#     serializer = StockSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def stockUpdate(request, pk):
#     item = Stock.objects.get(id=pk)
#     serializer = StockSerializer(instance=item, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
# @api_view(['DELETE'])
# def stockDelete(request, pk):
#     item = Stock.objects.get(id=pk)
#     item.delete()
#
#     return Response('Item succsesfully delete!')



class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class EquipmentViewSet(ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


# def add_stock(request):
    # item = StockSerializer(request.data)
    #
    # # validating for already existing data
    # if Stock.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
    #
    # if item.is_valid():
    #     item.save()
    #     return Response(item.data)
    # else:
    #     return Response(status=status.HTTP_404_NOT_FOUND)