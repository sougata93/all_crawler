from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
from playwright.sync_api import sync_playwright
import re
import os

url="https://www.adityabirlahealth.com/healthinsurance/downloads"
domain="https://www.adityabirlahealth.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def run(Q,FY):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.locator("text=PublicDisclosure").click()
        print(Q,FY)
        with page.expect_popup() as popup_info:

            page.locator("text="+Q+" - FY "+FY).click()
        
        page1 = popup_info.value
        print(page1)
        page1.wait_for_load_state()

        return page1.title()


year=['2021-22','2022-23']

quarter={'q1':'Q1','q2':'Q2','q3':'Q3','q4':'Q4'}

def yearFormat(year):
    year=re.sub('_','-',year)
    return year

def FYQ(year,Q):
    
    data=run(quarter[Q],yearFormat(year))
    print(data)

    if data==None:
        return
    soup=BeautifulSoup(data,'lxml')

    p=os.path.join('output',"nic_"+year+'_'+Q+".pdf")
    open(p, 'wb').write(data.content)

FYQ('22_23','q2')


        