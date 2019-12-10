from django.core.management.base import BaseCommand
from django.conf import settings

from fanpage.models import Photos, InvalidPage

from bs4 import BeautifulSoup
from io import BytesIO
from selenium import webdriver
from urllib.parse import urlparse

import json
import multiprocessing
import requests
import uuid
import time


env = settings.ENVIRONMENT


class Crontab(object):
    """ Crawler execution crontab class """
    def __init__(self, keyword):
        self.url = f"https://www.google.co.kr/search?q={keyword}&tbm=isch"
        self.keyword = keyword

    def execute_crawler(self):
        """ execute crawler return photos data"""
        print("*** Start Crawler ***")

        # check dev environment
        if env == "DEV":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome("chromedriver.exe", chrome_options=options)
        else:
            driver = webdriver.PhantomJS("phantomjs-2.1.1/bin/phandtomjs")

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
        print("LENGTH", len(html))
        image_data = list()
        extensions = ['jpg', 'jpeg', 'png', 'gif']

        for row in html:
            # 이미지, 이미지 게시 페이지 링크, 출처, 확장자, 제목, 넓이, 높이 추출
            row = json.loads(row.text)
            
            if row['ity'] in extensions:
                image_data.append({
                    "image": row['ou'],
                    "link": row['ru'],
                    "source": row['isu'],
                    "extension": row['ity'],
                    "title": row['pt'],
                    "width": row['ow'],
                    "height": row['oh'],
                })
        
        valid_data = self.page_valid_check(image_data)

        # SAVE IMAGE BY MULTIPROCESSING`
        if env == "DEV":
            self.save_photo(valid_data)
        else:
            pool = multiprocessing.Pool(processes=4)
            pool.map(self.save_photo, valid_data)
            pool.close()
            pool.join()

        # drvier 종료
        driver.close()
        print("*** driver close ***")

    def page_valid_check(self, data):
        """ valid check for response data, url etc.."""
        print("*** valid check ***")
        valid_data = list()

        for row in data:
            # 한번 크롤링한 링크는 다시 수집하지 않음
            if not Photos.objects.filter(link=row['link']).exists() and \
                not InvalidPage.objects.filter(url__startswith=row['link'].split("?")[0]).exists():
                valid_data.append(row)
            
            """
            # development test data
            if len(valid_data) > 30:
                break
            """
        return valid_data

    def save_photo(self, data):
        """ save for database """
        print("*** save photo ***")

        if env == "DEV":
            for row in data:
                try:
                    is_gif = True if row['extension'] == "gif" else False
                    
                    # 이미지 저장
                    p = Photos(link=row['link'], source=row['source'], is_gif=is_gif, title=row['title'],
                        width=row['width'], height=row['height'])
                    p.photo.save(f"{uuid.uuid4().hex}.{row['extension']}", BytesIO(requests.get(row['image']).content))

                    print(f"[SAVE PHOTO]: {row['title']}")
                except Exception as e:
                    print(f"[SAVE ERROR]: {row['title']} / {e}")
        else:
            row = data

            try:
                is_gif = True if row['extension'] == "gif" else False
                
                # 이미지 저장
                p = Photos(link=row['link'], source=row['source'], is_gif=is_gif, title=row['title'],
                    width=row['width'], height=row['height'])
                p.photo.save(f"{uuid.uuid4().hex}.{row['extension']}", BytesIO(requests.get(row['image']).content))

                print(f"[SAVE PHOTO]: {row['title']}")
            except Exception as e:
                print(f"[SAVE ERROR]: {row['title']} / {e}")
        print("COMPLETE!")


class Command(BaseCommand):
    help = "Crontab for crawling for days"

    def add_arguments(self, parser):
        parser.add_argument('keyword', type=str)

    def handle(self, *args, **options):
        keyword = options['keyword']

        cron = Crontab(keyword)
        cron.execute_crawler()
        
        del cron
