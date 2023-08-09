from rest_framework import serializers
from src.products.models import Tag, Product


class TagListingField(serializers.RelatedField):
 
     def to_representation(self, value):
         return value.name


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    tags = TagListingField(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category_name',
                  'price', 'created_at', 'tags')


class ProductsExportSerializer(serializers.Serializer):
    file = serializers.URLField(required=True)
