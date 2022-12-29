from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os
from playwright.sync_api import sync_playwright

url="https://www.aicofindia.com/AICEng/Pages/default.aspx" #playwright
domain="https://www.aicofindia.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def run(FY):
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.locator("text=Public Disclosure").click()
        # Select FY 2022-23
        print(FY)
        page.locator("#publicDisc").select_option("FY "+FY)
        
        return page.content()


year=['2021-22','2022-23']

quarter={'q1':'1st Quarter','q2':'2nd Quarter','q3':'3rd Quarter','q4':'4th Quarter'}

def yearFormat(year):
    year='20'+year
    year=re.sub('_','-',year)
    return year

def FYQ(year,Q):
    
    data=run(yearFormat(year))

    if data==None:
        return
    soup=BeautifulSoup(data,'lxml')
    x=soup.find('div',id='filterDiv')
    print(x)
    # p=os.path.join('output', "aic_"+year+"_"+Q+'_'+qText+".pdf")
    # open(p, 'wb').write(data.content)
    

FYQ('22_23','q2')


        