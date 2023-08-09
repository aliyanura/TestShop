from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from src.products.serializers import ProductSerializer
from src.products.services import ProductService


class productAPIView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductService.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]
    pagination_class = None
