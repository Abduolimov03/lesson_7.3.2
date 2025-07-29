from django.shortcuts import render
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Macbook
from .serializers import MacbookSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView

# class MacbookListView(ListAPIView):
#     serializer_class = MacbookSerializer
#     def get_queryset(self):
#         return Macbook.objects.all()
#
# class MacbookDetailView(RetrieveAPIView):
#     serializer_class = MacbookSerializer
#     def get_queryset(self):
#         return Macbook.objects.all()
#
# class MacbookDestroyView(DestroyAPIView):
#     serializer_class = MacbookSerializer
#     def get_queryset(self):
#         return Macbook.objects.all()
#
# class MacbookUpdateView(UpdateAPIView):
#     serializer_class = MacbookSerializer
#     def get_queryset(self):
#         return Macbook.objects.all()
#
# class MacbookCreateView(CreateAPIView):
#     serializer_class = MacbookSerializer
#     def get_queryset(self):
#         return Macbook.objects.all()

class MacbookApiView(APIView):
    def get(self, request):
        macbooks = Macbook.objects.all()
        serializer = MacbookSerializer(macbooks, many=True)
        data = {
            'macbooks':serializer.data,
            'status':status.HTTP_200_OK,
            'count':len(macbooks)
        }
        return Response(data)

    def post(self, request):
        serializer = MacbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Create Macbook', 'status':status.HTTP_201_CREATED})
        return Response({'status':status.HTTP_400_BAD_REQUEST})

class MacbookPKApiView(APIView):
    def delete(self, request, pk): #delete
        try:
            macbook = Macbook.objects.get(id=pk)
        except Macbook.DoesNotExist:
            return Response({'status':status.HTTP_400_BAD_REQUEST})
        macbook.delete()
        return Response({'status':status.HTTP_200_OK})

    def put(self, request, pk): #update
        macbook = Macbook.objects.get(id=pk)
        serializer = MacbookSerializer(macbook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_400_BAD_REQUEST})

    def putch(self, request, pk): #update
        macbook = Macbook.objects.get(id=pk)
        serializer = MacbookSerializer(macbook, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':status.HTTP_200_OK})
        return Response({'status':status.HTTP_400_BAD_REQUEST})

    def get(self, request, pk):
        try:
            macbook = Macbook.objects.get(id=pk)
        except Macbook.DoesNotExist:
            return Response({'status':status.HTTP_400_BAD_REQUEST})
        serializer = MacbookSerializer(macbook)
        return Response({
            'macbook':serializer.data,
            'status':status.HTTP_200_OK
        })
