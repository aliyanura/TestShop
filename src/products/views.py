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

    def export(self, request, *args, **kwargs):
        file = ProductService.get_file()
        serializer = ProductsExportSerializer({'file': file}, many=False)
        return Response(data={
            'result': serializer.data,
            'status': 'OK'
        }, status=status.HTTP_200_OK)
