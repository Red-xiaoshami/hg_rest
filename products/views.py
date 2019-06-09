from django.shortcuts import render
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics

from .models import ProductClass, CategoryClass
from .serializer import ProdectClassSerialiser, CategorySerializer


class ProductList(APIView):
    """
    List all products, or create a new snippet.
    """
    def get(self, request, format=None):
        products = ProductClass.objects.all()
        serializer = ProdectClassSerialiser(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProdectClassSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, pk):
        try:
            return ProductClass.objects.get(pk=pk)
        except ProductClass.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProdectClassSerialiser(products)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProdectClassSerialiser(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CategoryViewSet(generics.ListCreateAPIView):

    queryset = CategoryClass.objects.all()
    serializer_class = CategorySerializer

