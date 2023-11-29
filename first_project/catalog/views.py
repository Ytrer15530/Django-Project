from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from .models import Category, Goods, Tag
from .serializers import CategorySerializer, TagSerializer, GoodsSerializer
from .filters import GoodsFilter
from rest_framework.permissions import IsAuthenticated

from datetime import date
today = date.today()


class CategoryViews(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(activate=True).order_by('id').prefetch_related('goods', 'goods__tags')


class TagViews(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.order_by('id')


class GoodsViews(viewsets.ModelViewSet):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.filter(activate=True).order_by('id').prefetch_related('tags').select_related('category')
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_class = GoodsFilter
    permission_classes = [IsAuthenticated]
