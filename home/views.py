from django.shortcuts import render
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Macbook
from .serializers import MacbookSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework import mixins

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

# class MacbookApiView(APIView):
#     def get(self, request):
#         macbooks = Macbook.objects.all()
#         serializer = MacbookSerializer(macbooks, many=True)
#         data = {
#             'macbooks':serializer.data,
#             'status':status.HTTP_200_OK,
#             'count':len(macbooks)
#         }
#         return Response(data)
#
#     def post(self, request):
#         serializer = MacbookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message':'Create Macbook', 'status':status.HTTP_201_CREATED})
#         return Response({'status':status.HTTP_400_BAD_REQUEST})
#
# class MacbookPKApiView(APIView):
#     def delete(self, request, pk): #delete
#         try:
#             macbook = Macbook.objects.get(id=pk)
#         except Macbook.DoesNotExist:
#             return Response({'status':status.HTTP_400_BAD_REQUEST})
#         macbook.delete()
#         return Response({'status':status.HTTP_200_OK})
#
#     def put(self, request, pk): #update
#         macbook = Macbook.objects.get(id=pk)
#         serializer = MacbookSerializer(macbook, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':status.HTTP_200_OK})
#         return Response({'status':status.HTTP_400_BAD_REQUEST})
#
#     def patch(self, request, pk): #update
#         macbook = Macbook.objects.get(id=pk)
#         serializer = MacbookSerializer(macbook, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status':status.HTTP_200_OK})
#         return Response({'status':status.HTTP_400_BAD_REQUEST})
#
#     def get(self, request, pk):
#         try:
#             macbook = Macbook.objects.get(id=pk)
#         except Macbook.DoesNotExist:
#             return Response({'status':status.HTTP_400_BAD_REQUEST})
#         serializer = MacbookSerializer(macbook)
#         return Response({
#             'macbook':serializer.data,
#             'status':status.HTTP_200_OK
#         })


class ListCreateApi(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Macbook.objects.all()
    serializer_class = MacbookSerializer
    #
    # def get(self, request):
    #     macbooks = self.get_queryset()
    #     serializer = self.get_serializer(macbooks, many=True)
    #     data = {
    #         'data':serializer.data,
    #         'count': len(macbooks),
    #         'status':status.HTTP_200_OK
    #     }
    #     return Response(data)

    def get(self, request):
        return self.list(request)


    # def post(self, request):
    #     serializer = MacbookSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'message':'Create Macbook', 'status':status.HTTP_201_CREATED})
    #     return Response({'status':status.HTTP_400_BAD_REQUEST})

    def post(self, request):
        return self.create(request)


class DetailUpdateDeleteApi(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin , GenericAPIView):
    queryset = Macbook.objects.all()
    serializer_class = MacbookSerializer

    # def get_object(self, pk):
    #     macbook = Macbook.objects.get(id=pk)
    #     return macbook


    def get(self, request, pk):
        return self.retrieve(request, id=pk)

    def delete(self, request, pk):
        return self.destroy(request, id=pk)

    def put(self, request, pk):
        return self.update(request, id=pk)

    def patch(self, request, pk):
        return self.partial_update(request, id=pk)

    # def get(self, request, pk):
    #     book = self.get_object(pk=pk)
    #     serializer = MacbookSerializer(book)
    #     data = {
    #         'data': serializer.data,
    #         'status': status.HTTP_200_OK
    #     }
    #
    #     return Response(data)

    # def put(self, request, pk): #update
    #     macbook = Macbook.objects.get(pk=pk)
    #     serializer = MacbookSerializer(macbook, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status': status.HTTP_200_OK})
    #     return Response({'status':status.HTTP_400_BAD_REQUEST})

    # def patch(self, request, pk): #update
    #     macbook = Macbook.objects.get(pk=pk)
    #     serializer = MacbookSerializer(macbook, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'status':status.HTTP_200_OK})
    #     return Response({'status':status.HTTP_400_BAD_REQUEST})

    # def delete(self, request, pk): #delete
    #     try:
    #         macbook = Macbook.objects.get(id=pk)
    #     except Macbook.DoesNotExist:
    #         return Response({'status':status.HTTP_400_BAD_REQUEST})
    #     macbook.delete()
    #     return Response({'status':status.HTTP_200_OK})


