from rest_framework.permissions import IsAdminUser

from .models import Stock
from .serializers import StockSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response


"""Реализация CRUD для сущности складов"""
@api_view(['GET']) # Просмотр всех складов
@permission_classes([IsAdminOrReadOnly]) # Ограничение пользователей на изменение информации
def stockList(request):
    items = Stock.objects.all()
    serializer = StockSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST']) # Добавление склада
@permission_classes([IsAdminOrReadOnly])
def stockCreate(request):
    serializer = StockSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST']) # Изменение склада
@permission_classes([IsAdminOrReadOnly])
def stockUpdate(request, pk):
    item = Stock.objects.get(id=pk)
    serializer = StockSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE']) # Удаление выбранной склада
@permission_classes([IsAdminOrReadOnly])
def stockDelete(request, pk):
    item = Stock.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')