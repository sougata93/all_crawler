from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os



url="https://www.edelweissinsurance.com/web/motor/public-disclosure"
domain="https://www.edelweissinsurance.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')

year=['2021-22','2022-23']

def FY_22_23(year,Q):
    
    for x in res_n[0].xpath(".//div[@class='disclouserTabData year2023']//div[@id='quter22']//div[@class='item']//div[@class='row']"): #////row
        nlText=x.xpath(".//div[@class='finCardHd']//text()").extract()[0]
        nlNameText=x.xpath(".//div[@class='finCardDocName']//text()").extract()[0]
        nlLink=x.xpath(".//a//@href").extract()[0]
        nlLink=domain+nlLink
        print(nlText)
        print(nlNameText)
        nlText=nlText+nlNameText
        print(nlLink)
        data=requests.get(nlLink,headers=headers)
        print(data)
        p=os.path.join('output', "edelweiss_"+year+'_'+Q+'_'+nlText+".pdf")
        open(p, 'wb').write(data.content)
    


FY_22_23('22_23','Q2')
# FY_21_22('Q1')
# FY_21_22('Q2')
# FY_21_22('Q3')
# FY_21_22('Q4')

        