from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def create(self, validated_data):
        stock = Stock.objects.create(address=validated_data['address'])
        positions = validated_data['positions']
        stock_products = []
        for position in positions:
            position['stock'] = stock
            stock_products.append(StockProduct(**position))

        StockProduct.objects.bulk_create(stock_products)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for position in positions:
            position['stock'] = stock
            stock_product, created = StockProduct.objects.update_or_create(
                stock=stock,
                product_id=position['product'].id,
                defaults={
                    'quantity': position.get('quantity'),
                    'price': position.get('price')
                }
            )

        return stock
