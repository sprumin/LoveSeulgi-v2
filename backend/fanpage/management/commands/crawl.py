from django.core.management.base import BaseCommand

from fanpage.models import Album



class Crawler(object):
    def __init__(self, keyword):
        self.keyword = keyword

    def execute_crawler(self):
        # 내가 만든 크롤러인 Googler 사용예정
        pass


class Command(BaseCommand):
    help = "image crawler"

    def add_arguments(self, parser):
        parser.add_arguments("keyword", type=str)

    def handler(self, *args, **kwargs):
        keyword = kwargs["keyword"]

        c = Crawler(keyword)
        c.execute_crawler()