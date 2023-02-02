from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

from . models import MainCategory,SubCategory
from rest_framework import serializers
from .serializers import MainCategorySerializer,SubCategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView



class MainViewSet(APIView):
    queryset =MainCategory.objects.all()
    def get(self, request):
        query =MainCategory.objects.all()
        serializer = MainCategorySerializer(query,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MainCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


    def put(self, request, pk):
        query = MainCategory.objects.get(pk=pk)
        serializer = MainCategorySerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        print(pk)
        query = MainCategory.objects.filter(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubCategoryViewSet(APIView):
    queryset =SubCategory.objects.all()
    def get(self, request):
        query =SubCategory.objects.all()
        serializer = SubCategorySerializer(query,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


    


     

