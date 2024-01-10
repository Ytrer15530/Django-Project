import asyncio
import base64
import json
import aiohttp
import datetime
import aiofiles

from bs4 import BeautifulSoup

from slugify import slugify
from transliterate import translit

API_CATEGORY = 'http://127.0.0.1:8000/api/category/?format=json'
API_GOODS = 'http://127.0.0.1:8000/api/goods/?format=json'
URL_2 = 'https://ukrzoloto.ua'


async def req_body(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            body = await resp.text()
            return body


async def post_api(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as resp:
            print(await resp.json())
            return await resp.json()



def translit_word(name):
    return translit(name, 'ru', reversed=True)


async def download_image(good_img_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(good_img_url) as resp:
            img_data = await resp.read()
            b_img = base64.b64encode(img_data).decode('utf-8')  # Тут потрібно байт файла перевести в base64

            return b_img



async def parse():
    startTime = datetime.datetime.now()
    print('Start')
    content = await req_body(URL_2 + '/catalog')
    bs = BeautifulSoup(content, 'html5lib')

    for item in bs.findAll("a", {"class": "catalogue-categories__link"}):
        name = item.get_text()
        if name == 'Сертификаты':
            break

        category_json = {
            'name': name,
            'activate': True,
            'url': str(item),
        }
        print(name)

        category = await post_api(API_CATEGORY, category_json)
        category_id = category.get('id')

        good_url = URL_2 + item['href']
        goods_content = await req_body(good_url)
        bs1 = BeautifulSoup(goods_content, 'html5lib')
        goods = bs1.findAll("div", {"class": "product-card__content"})
        for index, good_item in enumerate(goods):
            good_name = good_item.select_one('.title').get_text()
            good_img_url = good_item.select_one('.image')['src']
            good_price = good_item.select_one('.price__current span').get_text().replace(' ', '')
            price_opt = good_item.select_one('.price__old span').get_text().replace(' ', '')

            goods_json = {
                'category':category_id,
                'name': f'{good_name}',
                'description':translit_word(good_name),
                'price_opt':price_opt,
                'price':good_price,
                'activate':True,
                'image': await download_image(good_img_url)
            }
            await post_api(API_GOODS, goods_json)



    print("Used time:", datetime.datetime.now() - startTime)



main_loop = asyncio.get_event_loop()


if __name__ == '__main__':
    main_loop.run_until_complete(parse())
    #main_loop.run_forever()