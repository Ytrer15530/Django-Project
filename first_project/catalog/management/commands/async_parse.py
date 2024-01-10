import asyncio
import aiohttp
import datetime
import aiofiles
import aiohttp
from catalog.models import Category, Goods
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from django.conf import settings
from django.utils.translation import gettext
from django.template.defaultfilters import slugify
from transliterate import translit


URL = 'https://ukrzoloto.ua'

async def req_body(url):
    async with aiohttp.ClientSession as session:
        async with session.get(url) as resp:
            body = await resp.text()
            return body


def translit_word(name):
    return translit(name, 'ru', reversed=True)


async def download_image(good_img_url, image_name):
    async with aiohttp.ClientSession as session:
        async with session.get(good_img_url) as resp:
            img_data = await resp.read()
    image_src = f'{settings.BASE_DIR}\media\{image_name}.jpg'
    async with aiofiles.open(image_src, 'wb') as handler:
        await handler.write(img_data)
    return image_src


async def parse():
    print('Start')
    content = await req_body(URL + '/catalog')
    bs = BeautifulSoup(content, 'html5lib')

    for item in bs.findAll("a", {"class": "catalogue-categories__link"}):
        name = item.get_text()
        print(name)
        activate = True
        url = str(item)
        category = Category.objects.get_or_create(name=name, activate=activate, url=url)
        good_url = URL + item['href']
        goods_content = await req_body(good_url)
        bs1 = BeautifulSoup(goods_content, 'html5lib')
        goods = bs1.findAll("div", {"class": "product-card__content"})
        for index, good_item in enumerate(goods):
            good_name = good_item.select_one('.title').get_text()
            good_img_url = good_item.select_one('.image')['src']
            good_price = good_item.select_one('.price__current span').get_text().replace(' ', '')
            print(good_price)
            goods, created = Goods.objects.get_or_create(
                category=category[0],
                name=f'{good_name} + {index}',
                description=translit_word(good_name),
                price=good_price,
                activate=True,
                image=download_image(good_img_url, slugify(translit_word(good_name))),
            )
            print(goods, created)


class Command(BaseCommand):
    async def handle(self, *args, **options):
        await parse()


main_loop = asyncio.get_event_loop()


if __name__ == '__main__':
    main_loop.run_until_complete()
