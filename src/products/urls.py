from django.urls import path
from src.products import views


urlpatterns = [
    path('products/', views.productAPIView.as_view({'get': 'list'}), name='products'),
    path('products/export/', views.productAPIView.as_view({'get': 'export'}), name='products-export'),
]