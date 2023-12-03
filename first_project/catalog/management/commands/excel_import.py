from django.core.management.base import BaseCommand
import requests
from openpyxl import Workbook
url_token = "http://127.0.0.1:8000/api/token/"
url_cat = "http://127.0.0.1:8000/api/category/"
url_goods = 'http://127.0.0.1:8000/api/goods/'
wb = Workbook()
ws = wb.active


class Command(BaseCommand):
    def handle(self, *args, **options):
        username = input('Enter user name ')
        password = input('Enter password ')
        res_token = requests.post(url_token, data={f'username': username, 'password': password})
        access_token = res_token.json().get('access')
        res_category = requests.get(url_cat, headers={'Authorization': f'Bearer {access_token}'})
        res_goods = requests.get(url_goods, headers={'Authorization': f'Bearer {access_token}'})

        if res_category.status_code == 200:
            category_json = res_category.json().get('results')
            title = ['Category', 'Goods']
            ws.append(title)
            for category in category_json:
                category_name = category.get('name')
                if res_goods.status_code == 200:
                    goods_json = res_goods.json().get('results')
                    for item in goods_json:
                        if item.get('category') == category_name:
                            good_name = item.get('name')
                            ws.append([category_name, good_name])
        wb.save('pythontesst.xlsx')






