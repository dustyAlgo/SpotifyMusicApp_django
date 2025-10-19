from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room
#from django.http import HttpResponse
# Create your views here.
#def main(request):
#    return HttpResponse("<h1> Hello guisss :) </h1>")
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    

