from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
from selenium import webdriver

import json
import time


class Crontab(object):
    """ Crawler execution crontab class """
    def __init__(self, keyword):
        self.url = f"https://www.google.co.kr/search?q={keyword}&tbm=isch"
        self.keyword = keyword

    def execute_crawler(self):
        """ execute crawler return photos data"""
        # Selenium
        driver = webdriver.Chrome("chromedriver.exe")
        driver.implicitly_wait(3)
        driver.get(self.url)

        # Full Scroll
        last_height = driver.execute_script("return document.body.scrollHeight")
        pause = 0.5

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)

            try:
                element = driver.find_elements_by_id("smb")[0]
                element.click()
            except:
                pass

            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break

            last_height = new_height

        res = BeautifulSoup(driver.page_source, "html.parser")

        html = res.find_all("div", {"class": "rg_meta notranslate"})

        for row in html:
            # 이미지링크, 확장자, 제목, 넓이, 높이
            print(json.loads(row['ou'], row['ity'], row['pt'], row['ow'], row['oh']))
            break

        # drvier 종료
        driver.close()

    def page_valid_check(self):
        """ valid check for response data, url etc.."""
        pass

    def save_photo(self):
        """ save for database """
        pass


class Command(BaseCommand):
    help = "Crontab for crawling for days"

    def add_arguments(self, parser):
        parser.add_argument('keyword', type=str)

    def handle(self, *args, **options):
        keyword = options['keyword']

        cron = Crontab(keyword)
        cron.execute_crawler()
        del cron