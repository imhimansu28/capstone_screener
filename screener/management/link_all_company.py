import io
import os
import shutil
import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

DOWNLOAD_PATH = (
    "/home/himanshu/Downloads"
)
def all_company_list():
    """
    sumary_line: Get all company list from BSE
    save all company list to csv file
    
    """
    filepath =  os.path.join(DOWNLOAD_PATH, "Equity.csv")
    url = "https://www.bseindia.com/corporates/List_Scrips.html"

    remove_file  = os.path.isfile(filepath)
    if remove_file:
        os.remove(filepath)

    driver_path = "utilities/chromedriver"
    driver = Chrome(executable_path=driver_path)
    
    driver.get(url)
    select = Select(driver.find_element(By.ID, "ddlsegment"))
    select.select_by_value("Equity")
    select = Select(driver.find_element(By.ID, "ddlstatus"))
    select.select_by_value("Active")
    driver.execute_script("document.getElementById('btnSubmit')" ".click()")
    select = driver.find_element(By.ID, "lnkDownload")
    select.click()
    options = webdriver.ChromeOptions() 
    options.add_argument("download.default_directory=" + DOWNLOAD_PATH)
    
    time.sleep(10)
    driver.quit()

    print("done")

