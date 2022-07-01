import csv

from django.core.management.base import BaseCommand, CommandError
from screener.management.scrap_company_list import all_company_list

from screener.models import Company


class Command(BaseCommand):
    help = 'Link companies to BSE'

    def handle(self, *args, **options):
        all_company_list()
        link_company()
        return 0


def link_company():
    with open('/home/himanshu/Downloads/Equity.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            link_company = Company.objects.get_or_create(
                    company_id=row[0],
                    company_name=row[1],
                    company_code=row[2],
                    company_group=row[5],
                    company_industry=row[8],
                    isin_number=row[7]

                )
        
