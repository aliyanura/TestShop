from src.products.models import Product
from src.common.services import Service


class ProductService(Service):
    model = Product
