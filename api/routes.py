from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
  path('auth', obtain_auth_token),
  path('home', views.api_home),
  path('product', views.listProducts),
  path('products', views.products),
  path('prodsView', views.ProductListView.as_view()),
  path('create', views.ProductCreateView.as_view()),
  path('createList', views.ProductListCreateView.as_view()),
  path('update', views.ProductUpdateView.as_view()),
  path('product/<int:pk>', views.ProductDetailsView.as_view()),
  path('prod/<int:pk>/update', views.ProductUpdateView.as_view()),
  path('prod/<int:pk>/delete', views.ProductDestroyView.as_view()),
]
