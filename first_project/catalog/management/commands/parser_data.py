from django.core.management.base import BaseCommand
from catalog.models import Category, Goods
import requests
from bs4 import BeautifulSoup