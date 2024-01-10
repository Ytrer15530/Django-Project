from rest_framework import serializers
from .models import Category, Goods, Tag
from drf_extra_fields.fields import Base64ImageField


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'uuid']


class GoodsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = Base64ImageField(required=False)
    # category = serializers.CharField(source='category.name')
    # parametr = serializers.CharField(source='parametr.name')
    parametr = serializers.SerializerMethodField()

    class Meta:
        model = Goods
        fields = ['id', 'name', 'description', 'price', 'activate', 'created', 'image', 'tags', 'category',
                  'parametr']


    def get_parametr(self,goods):
        try:
            parametr_name = goods.parametr.name
            return parametr_name
        except Exception:
            return 'no name'


class CategorySerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True, read_only=True)
    goods_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'activate', 'created', 'goods', 'goods_count']

    def get_goods_count(self, category):
        count = category.goods.count()
        return count

    def to_internal_value(self, data):
        name = data.get('name')
        existing_category = Category.objects.filter(name=name).first()

        if existing_category:
            return CategorySerializer(existing_category).data
        return super().to_internal_value(data)
