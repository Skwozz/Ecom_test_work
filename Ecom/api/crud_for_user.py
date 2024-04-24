from .models import User
from .permissions import IsAdminOrReadOnly
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import Response

@api_view(['GET'])
def userList(request):
    items = User.objects.all()
    serializer = UserSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def userCreate(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def userUpdate(request, pk):
    item = User.objects.get(id=pk)
    serializer = UserSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminOrReadOnly])
def userDelete(request, pk):
    item = User.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')