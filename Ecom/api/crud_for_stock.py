from .models import Stock
from .serializers import StockSerializer
from rest_framework.decorators import api_view
from rest_framework.views import Response

@api_view(['GET'])
def stockList(request):
    items = Stock.objects.all()
    serializer = StockSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def stockCreate(request):
    serializer = StockSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def stockUpdate(request, pk):
    item = Stock.objects.get(id=pk)
    serializer = StockSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def stockDelete(request, pk):
    item = Stock.objects.get(id=pk)
    item.delete()

    return Response('Item succsesfully delete!')