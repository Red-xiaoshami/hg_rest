from .models import ProductClass, CategoryClass
from rest_framework import serializers

# class CategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = CategoryClass
#         fields = ('url', 'name')
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     category = serializers.CharField(source='category.id')
#     category_name = serializers.CharField(source='category.name')
#
#     class Meta:
#         model = ProductClass
#         fields = ('name', 'price', 'count', 'category', 'category_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryClass
        fields = ('url', 'name')

#
class ProdectClassSerialiser(serializers.ModelSerializer):
    # 第一种方法
    category = serializers.IntegerField(source='category.id')
    category_name = serializers.CharField(source='category.name')

    # 第二种方法
    # category_id = serializers.ReadOnlyField()
    # category_name = serializers.ReadOnlyField()

    class Meta:
        model = ProductClass
        fields = ('name', 'price', 'count', 'category', 'category_id', 'category_name')
# 第二种方法的结果
# [
#     {
#         "name": "猪肉",
#         "price": "22.00",
#         "count": 100,
#         "category": 1,
#         "category_id": 1,
#         "category_name": [
#             1,
#             "肉类"
#         ]
#     },
#     {
#         "name": "面粉",
#         "price": "5.00",
#         "count": 54,
#         "category": 3,
#         "category_id": 3,
#         "category_name": [
#             3,
#             "粮油"
#         ]
#     }
# ]
#
# class ProdectClassSerialiser(serializers.ModelSerializer):
#     class Meta:
#         model = ProductClass
#         fields = ('id', 'name', 'price', 'count', 'category')
#
#
class CategorySerializer(serializers.ModelSerializer):
    products_set = ProdectClassSerialiser(many=True)
    class Meta:
        model = CategoryClass
        fields = ('id', 'name', 'products_set')

# [
#     {
#         "id": 1,
#         "name": "肉类",
#         "products_set": [
#             {
#                 "name": "猪肉",
#                 "price": "22.00",
#                 "count": 100,
#                 "category": 1,
#                 "category_id": 1,
#                 "category_name": "肉类"
#             },
#             {
#                 "name": "排骨",
#                 "price": "26.00",
#                 "count": 199,
#                 "category": 1,
#                 "category_id": 1,
#                 "category_name": "肉类"
#             }
#         ]
#     },
#     {
#         "id": 2,
#         "name": "水果",
#         "products_set": []
#     },
#     {
#         "id": 3,
#         "name": "粮油",
#         "products_set": [
#             {
#                 "name": "面粉",
#                 "price": "5.00",
#                 "count": 54,
#                 "category": 3,
#                 "category_id": 3,
#                 "category_name": "粮油"
#             }
#         ]
#     },
#     {
#         "id": 4,
#         "name": "服装",
#         "products_set": []
#     }
# ]
