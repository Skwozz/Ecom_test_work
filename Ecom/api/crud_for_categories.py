from .models import Category
from .serializers import CategorySerializer
from rest_framework.views import Response
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAdminOrReadOnly])
def categoryList(request):
    items = Category.objects.all()
    serializer = CategorySerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def categoryCreate(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminOrReadOnly])
def categoryUpdate(request, pk):
    item = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminOrReadOnly])
def categoryDelete(request, pk):
    item = Category.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')