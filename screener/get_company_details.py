
from selenium import webdriver

from .models import Company


def get_bse_url(company_id):
    url = "https://www.bseindia.com/corporates/CompanyTrackerData.aspx?scripcode=" + company_id
    driver = webdriver.Chrome()
    driver.get(url)
    return url
    

def open_url():
    company = Company.objects.all()
    for comp in company:
        company_id = comp.company_id
        get_bse_url(company_id)
