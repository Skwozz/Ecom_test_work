from .models import User
from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response


"""Реализация CRUD для сущности пользователя"""
@api_view(['GET'])# Просмотр всех пользователей
def userList(request):
    items = User.objects.all()
    serializer = UserSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST']) # Добавление/регистрация пользователя
def userCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST']) # Добавление/регистрация пользователя
@permission_classes([IsAdminOrReadOnly])
def userUpdate(request, pk):
    item = User.objects.get(id=pk)
    serializer = UserSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE']) # Удаление выбранного пользователя
@permission_classes([IsAdminOrReadOnly])
def userDelete(request, pk):
    item = User.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')