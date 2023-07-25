from rest_framework import viewsets
from api.models import Product
from api.serializers import ProductSerializers


class ProductViewSet(viewsets.ModelViewSet):
  """
  get -> list ->queryset
  get -> retrieve -> product instance detail view
  post -> create -> New Instance
  put -> update
  patch -> partial update
  delete -> destroy
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'
