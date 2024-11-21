from rest_framework import serializers

from product import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = "__all__"


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        # fields = ['name', 'subcategory', 'address', 'price', 'start_time', 'end_time', 'start_day', 'end_day']
        fields = "__all__"
        extra_kwargs = {'user': {'required': False}}


    def create(self, validated_data):
        print(self.context['request'].user)
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"
