from django.core.management.base import BaseCommand



class Crontab(object):
    """ Crawler execution crontab class """
    def __init__(self, keyword):
        self.url = f"https://www.google.co.kr/search?q={keyword}"
        self.keyword = keyword

    def execute_crawler(self):
        """ execute crawler return photos data"""
        pass

    def page_valid_check(self):
        """ valid check for response data, url etc.."""
        pass

    def save_photo(self):
        """ save for database """
        pass


class Command(BaseCommand):
    help = "Crontab for crawling for days"

    def add_arguments(self, parser):
        parser.add_arguments('keyword', type=str)

    def handle(self, *args, **kwargs):
        keyword = options['keyword']

        cron = Crontab(keyword)
        cron.execute_crawler()
        del cron