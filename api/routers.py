from rest_framework.routers import DefaultRouter
from api.ViewSets import ProductViewSet

routes = DefaultRouter()
routes.register('products', ProductViewSet, basename='products')

urlpatterns = routes.urls
