from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from product import models, serializers
from config import permissions


class CategoryListAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategorySubCategoryListView(APIView):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer

    def get(self, request, category_id):
        subcategories = models.SubCategory.objects.filter(category_id=category_id)
        serializer = serializers.SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class SubCategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.SubCategory.objects.all()
    serializer_class = serializers.SubCategorySerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        return [permissions.BusinessUserPermission()]


class ProductBusinessUserAPIView(APIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get(self, request):
        products = models.Product.objects.filter(user=request.user)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        return [permissions.BusinessUserPermission()]


class SubCategoryProductAPIView(APIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get(self, request, subcategory_id):
        products = models.Product.objects.filter(subcategory_id=subcategory_id)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
