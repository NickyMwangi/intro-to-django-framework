from rest_framework import serializers
from .models import Product


class ProductInlineSerializer(serializers.Serializer):
  url = serializers.HyperlinkedIdentityField(
    view_name='product-detail',
    lookup_field='pk',
    read_only=True
  )
  title = serializers.CharField(read_only=True)


class ProductSerializers(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = [
      'pk',
      'title',
      'description',
      'price',
      'sale_price'
    ]
