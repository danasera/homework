from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from django.views import generic
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductListSerializer, ProductDetailSerializer, CreateProductSerializer


class ProductsListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'id'


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer


@api_view(['GET'])
def first_product(request):
    product = Product.objects.all()
    serializer = ProductListSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_details(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductDetailSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = CreateProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['PATCH'])
def patch_product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = CreateProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Successfully delete")


@api_view(['POST'])
def create_product(request):
    serializer = CreateProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    lookup_url_kwarg = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return CreateProductSerializer