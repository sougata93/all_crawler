from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os
from playwright.sync_api import sync_playwright
from zipfile import ZipFile


url="https://nationalinsurance.nic.co.in/en/about-us/business-performance"
domain="https://nationalinsurance.nic.co.in"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def run():
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        page.locator("#ui-accordion-1-header-2 span").click()
        return page.content()

year=['2021-22','2022-23']

quarter={'q1':['Q1','first'],'q2':['Q2','second'],'q3':['Q3','third'],'q4':['Q4','fourth']}
def match(Q,nlText):
    flag=0
    for i in quarter[Q]:
        if i.lower() in nlText.lower():
            flag=1
            return True
    if flag==0:
        return False

def yearFormat(year):
    year='20'+year
    year=re.sub('_','-',year)
    return year

def FYQ(year,Q):
    
    data=run()

    if data==None:
        return
    soup=BeautifulSoup(data,'lxml')

    span=soup.find('div',id='ui-accordion-1-panel-2')
    t=span.find_all('div',class_='field-content')

    for i in t:
        nlDoc=i.find('a')
        if nlDoc!=None:
            nlText=nlDoc.text
            nlLink=nlDoc.get('href')
            print(nlText)
            print(nlLink)
            if yearFormat(year) in nlText and match(Q,nlText):
                pdfData=requests.get(nlLink,verify=False)
                p=os.path.join('output',"nic_"+year+'_'+Q+'_'+nlText+".zip")
                open(p, 'wb').write(pdfData.content)

                with ZipFile(p, 'r') as zipObj:
                    zipObj.extractall(path='output')
    
FYQ('22_23','q2')


        