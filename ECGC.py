from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os


url="https://main.ecgc.in/english/public-disclosures/"
domain="https://main.ecgc.in"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')



year=['2021-22','2022-23']

def FY_22_23(Q):
    
  
    #Quarter=res_n[0].xpath("//div[@data-year='2022-23']//div[@class='deviceFinanceTabHeads']//text()")[0].extract()
    for x in res_n[0].xpath(".//ul[@class='pc1']//ul[@class='pc1']//li//a"):
        
        textFYQ=x.css("::text")[0].extract()
        print(textFYQ)
        
        if not re.search(Q,textFYQ):
            continue
        
        qLink=x.xpath("@href")[0].extract()
        qLink=url+qLink
        print(qLink)
        nlPage = requests.get(qLink,headers=headers)
        response=Selector(nlPage)
        resp=response.css('body')
        print(nlPage)
        for y in resp[0].xpath(".//div[@class='col span_8_of_12']//div[@class='col span_4_of_12']//a"):
            nlText=y.css("::text")[0].extract()
            nlText=re.sub('/','',nlText)
            print(nlText)
            nlLink=y.xpath("@href").extract()[0]
            if(len(nlLink)!=0):
                
                nlLink=nlLink.replace("\\",'/')
                print(nlLink)
                data = requests.get(nlLink,headers=headers)
                p=os.path.join('output', "ECGC_"+textFYQ+"_"+nlText+".pdf")
                open(p, 'wb').write(data.content)

FY_22_23('Second Quarter')
# FY_21_22('Q1')
# FY_21_22('Q2')
# FY_21_22('Q3')
# FY_21_22('Q4')

        