from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os

url="https://general.futuregenerali.in/about-us/financial-information#publicDisclosure"
domain="https://general.futuregenerali.in"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')

year=['2021-22','2022-23']

quarter={'q1':'1st Quarter','q2':'2nd Quarter','q3':'3rd Quarter','q4':'4th Quarter'}

def yearFormat(year):
    year='20'+year
    year=re.sub('_','-',year)
    return year

def FYQ(year,Q):
    
    for x in res_n[0].xpath(".//section[@class='investorInformationComp']//div[@class='subAccordianWrap']//div[@class='subAccordianContent']//div[@class='publicDisclosuresWrap']//ul//li"): #//ul//li
        qText=x.xpath(".//a//text()").extract()[0]
        nlLink=x.xpath(".//a//@href").extract()[0]
        yearText=x.xpath(".//a//@data-category").extract()[0]
        print(qText)
        print(nlLink)
        print(yearText)
        if 'egm' in nlLink.lower():
            continue
        
        if yearFormat(year) in yearText and quarter[Q] in qText.lower():
            data=requests.get(nlLink,headers=headers)
            print(data)
            p=os.path.join('output', "future_"+year+"_"+qText+".pdf")
            open(p, 'wb').write(data.content)
    

FYQ('22_23','q2')


        