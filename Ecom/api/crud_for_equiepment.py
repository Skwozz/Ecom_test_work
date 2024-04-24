from .models import Equipment
from .serializers import EquipmentSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response


"""Реализация CRUD для сущности оборудования"""
@api_view(['GET']) # Просмотр всего оборудования
@permission_classes([IsAdminOrReadOnly])# Ограничение пользователей на изменение информации
def equipmentList(request):
    items = Equipment.objects.all()
    serializer = EquipmentSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST']) # Добавление оборудования
@permission_classes([IsAdminOrReadOnly])
def equipmentCreate(request):
    serializer = EquipmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST']) # Изменение информации об оборудования
@permission_classes([IsAdminOrReadOnly])
def equipmentUpdate(request, pk):
    item = Equipment.objects.get(id=pk)
    serializer = EquipmentSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE']) # Удаление выбранного оборудования
@permission_classes([IsAdminOrReadOnly])
def equipmentDelete(request, pk):
    item = Equipment.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')


