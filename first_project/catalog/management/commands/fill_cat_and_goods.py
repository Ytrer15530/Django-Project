from django.core.management.base import BaseCommand
import requests
from catalog.models import Category, Goods
import random

URL_CATEGORY = "https://api.escuelajs.co/api/v1/categories"
# URL_GOODS = "https://api.escuelajs.co/api/v1/products"
url_goods = "https://reqres.in/api/{resource}?page=1&per_page=12"


class Command(BaseCommand):

    def handle(self, *args, **options):
        res_cat = requests.get(URL_CATEGORY)
        res_goods = requests.get(url_goods)
        goods_list = []
        cat_list = []
        for category_item in res_cat.json():
            cat_name = category_item['name']
            print(cat_name)
            category, created = Category.objects.get_or_create(name=cat_name)
            cat_list.append(category)
        for goods_item in res_goods.json()['data']:
            good_name = goods_item['name']
            if good_name not in goods_list:
                goods_list.append(good_name)
                Goods.objects.create(name=good_name, category=random.choice(cat_list))
        print('finish')

