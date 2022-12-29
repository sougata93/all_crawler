from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os



url="https://www.cholainsurance.com/about-us/public-disclosure"
domain="https://www.cholainsurance.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')

year=['2021-22','2022-23']

def FY_22_23(Q):
    
    for x in res_n[0].xpath(".//div[@id='home-3']//div[@class='fact-tab-content public-disclosures-2022-23']"):
        
        qText=x.xpath(".//div//text()").extract()[0]      
        print(qText)
        if not Q in qText:
            continue
        nlLink=x.xpath(".//div//a//@href").extract()[1]
        nlLink=domain+nlLink
        print(nlLink)
        data=requests.get(nlLink,headers=headers)
        print(data)
        p=os.path.join('output', "cholainsurance_"+qText+".pdf")
        open(p, 'wb').write(data.content)
        
        
        
            
        
        #textFYQ=x.css("::text").extract()[0]
        #print(textFYQ)


FY_22_23('Q1')
# FY_21_22('Q1')
# FY_21_22('Q2')
# FY_21_22('Q3')
# FY_21_22('Q4')

        