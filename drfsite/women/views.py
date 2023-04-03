from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import WomenSerializer
# Create your views here.


class WomenAPIList(ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDetailView(RetrieveUpdateDestroyAPIView ):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenApiView(APIView):
#     def get(self, request):
#         posts = Women.objects.all()
#         return Response({'posts': WomenSerializer(posts, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method Put not allowed'})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method Put not allowed'})
#
#         try:
#             instance = Women.objects.get(pk=pk).delete()
#         except:
#             return Response({'error': 'Object does not exists'})
#
#         return Response({'post': "delete post " + str(pk)})


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


