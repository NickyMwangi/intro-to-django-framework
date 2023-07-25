import json
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProductSerializers
from api.models import Product
from django.http import JsonResponse
from django.forms.models import model_to_dict
from api.permissions import DataCapturerPermission
from api.mixins import DataCapturerPermissionMixins


# intro
# Create your views here.
def api_home(request, *args, **kwargs):
  body = request.body
  data = {}
  try:
    data = json.loads(body)
  except:
    pass

  data['headers'] = request.headers
  data['content_type'] = request.content_type
  print(data)
  return JsonResponse({"detail": "Hello there! This is my Django project APi"})


def listProducts(request, *args, **kwargs):
  model_data = Product.objects.all().order_by("?").first()
  data = {}
  data_with_fields = {}
  if model_data:
    data = model_to_dict(model_data)
    data_with_fields = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])

  return JsonResponse(data_with_fields)


# Rest Framework Implementations
@api_view(["GET", "POST"])
def products(request, *args, **kwargs):
  data = {}
  if request.method == 'POST':
    product = ProductSerializers(data=request.data)
    if product.is_valid(raise_exception=True):
      instance = product.save()
      print(instance)
      return Response(product.data)
  else:
    instance = Product.objects.all().order_by("?").first()
    if instance:
      data = ProductSerializers(instance).data
    return Response(data)


class ProductListView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  permission_classes = [permissions.IsAuthenticated, DataCapturerPermission]


class ProductDetailsView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  permission_classes = [permissions.IsAuthenticated, DataCapturerPermission]


class ProductCreateView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  permission_classes = [permissions.IsAuthenticated]

  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    title = serializer.validated_data.get('title')
    description = serializer.validated_data.get('description') or None
    if description is None:
      description = title
    serializer.save(description=description)
    # send Django signal


class ProductUpdateView(generics.RetrieveUpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  permission_classes = [permissions.IsAuthenticated]
  lookup_field = 'pk'


class ProductListCreateView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers

  permission_classes = [permissions.IsAuthenticated, permissions.DjangoModelPermissions]


@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
  if request.method == "GET":
    if pk is None:
      queryset = Product.objects.all()
      data = ProductSerializers(queryset, many=True)
      return Response(data)
    queryset = Product.objects.filter(pk=pk)
    data = ProductSerializers(queryset, many=True)
    return Response(data)
  elif request.method == "POST":
    serializer = ProductSerializers(data=request.data)
    if (serializer.is_valid(raise_exception=True)):
      serializer.save()
      return serializer.data


class ProductDestroyView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  permission_classes = [permissions.IsAuthenticated]
  lookup_field = 'pk'


# List all the views together
class ProductMixinView(mixins.ListModelMixin, DataCapturerPermissionMixins,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers
  lookup_field = 'pk'

  def post(self, request, *args, **kwargs):
    return self.list(request, args, kwargs)
