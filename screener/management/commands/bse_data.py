import csv
import os
from email import parser
from lib2to3.pgen2 import driver
from webbrowser import Chrome

from django.core.management.base import BaseCommand, CommandError

from screener.management.link_all_company import all_company_list
from screener.models import Company


class Command(BaseCommand):
    help = 'Link companies to BSE'
    
    def handle(self, *args, **options):
       
        if os.path.isfile('/home/himanshu/Downloads/Equity.csv'):
            link_company()
        else:
            all_company_list()
            link_company()
        return 0


def link_company():
    if os.path.isfile('/home/himanshu/Downloads/Equity.csv'):
        with open('/home/himanshu/Downloads/Equity.csv') as file:
            reader =  csv.reader(file)
            # check if company_id is already present in database
            for row in reader:

                link_company = Company.objects.filter(company_id=row[0])
                if link_company:
                    pass
                else:
                    companyName = row[1].lower().replace(' ', '-')
                    link_company = Company.objects.get_or_create(
                        company_id=row[0],
                        company_name=row[1],
                        company_code=row[2],
                        company_group=row[5],
                        company_industry=row[8],
                        isin_number=row[7],
                        slug = companyName
                        )
        
        print("Add done !!!")
                
        



    
