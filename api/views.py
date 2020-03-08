from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from features.models import Direction
from api.serializers import DirectionSerializer
# Create your views here.

# class DirectionList(APIView):
#     def get(self, request):
#         directions = Direction.objects.all()[:20]
#         data = DirectionSerializer(directions, many=True).data
#         return Response(data)

# class DirectionDetail(APIView):
#     def get(self, request, pk):
#         direction = get_object_or_404(Direction, pk=pk)
#         data = DirectionSerializer(direction).data
#         return Response(data)
    
class DirectionList(ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionDetail(RetrieveDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer