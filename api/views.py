from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from features.models import Direction
from api.serializers import DirectionSerializer
# Create your views here.
    
class DirectionList(ListCreateAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

class DirectionDetail(RetrieveDestroyAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer