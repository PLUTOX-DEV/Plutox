
from django.contrib.auth.decorators import permission_required
from rest_framework.decorators import api_view   
from rest_framework.response import Response
from base.models import Room
from .serializers import RommSerializer

@permission_required
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET /api / rooms',
        'GEt / api/ rooms/:id'
    ]
    return Response(routes,)


@permission_required
@api_view(['GET'])
def getRooms(request):   
    rooms = Room.objects.all()
    serializer = RommSerializer(rooms, many=True)
    return Response(serializer.data)

@permission_required
@api_view(['GET'])
def getRoom(request, pk):   
    room = Room.objects.get(id=pk)
    serializer = RommSerializer(room, many=False)
    return Response(serializer.data)