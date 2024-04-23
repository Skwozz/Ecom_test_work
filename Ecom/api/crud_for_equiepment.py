from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework.decorators import api_view
from rest_framework.views import Response

@api_view(['GET'])
def equipmentList(request):
    items = Equipment.objects.all()
    serializer = EquipmentSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def equipmentCreate(request):
    serializer = EquipmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def equipmentUpdate(request, pk):
    item = Equipment.objects.get(id=pk)
    serializer = EquipmentSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def equipmentDelete(request, pk):
    item = Equipment.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')


