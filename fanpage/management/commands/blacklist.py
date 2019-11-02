from django.core.management.base import BaseCommand

from fanpage.models import InvalidPage


class Command(BaseCommand):
    help = "Invalid Page append Database"

    def handle(self, *args, **options):
        blacklist = [
            {"url": "http://www.sportalkorea.com/butterfly/view.php"},
        ]

        for row in blacklist:
            if row['url']:
                InvalidPage(url=row['url'])
            elif row['content']:
                InvalidPage(content=row['content'])
            else:
                print("[BlackList Error] Invalid Data.")

        print("COMPLETE!")