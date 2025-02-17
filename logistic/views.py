from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.filters import SearchFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description',]
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [SearchFilter]
<<<<<<< HEAD
    search_fields = ['products__title','products__description']
=======
    search_fields = ['positions__product__title',]
>>>>>>> 166e5ea1628d55ff3aee12e59fa7238adfdd20d4
    # при необходимости добавьте параметры фильтрации
