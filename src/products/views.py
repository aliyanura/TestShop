from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from src.products.serializers import ProductSerializer,\
                                     ProductsExportSerializer
from src.products.services import ProductService


class productAPIView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductService.filter(is_deleted=False)
    permission_classes = [IsAuthenticated]
    pagination_class = None

    @cache_page(60 * 60 * 6) # cache for 6 hours
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def export(self, request, *args, **kwargs):
        file = ProductService.get_file()
        serializer = ProductsExportSerializer({'file': file}, many=False)
        return Response(data={
            'result': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)
