from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os

url="https://www.iffcotokio.co.in/about-us/public-disclosure"
domain="https://www.iffcotokio.co.in"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')




quarter={'q1':['june','Q1'],'q2':['september','Q2'],'q3':['december','Q3'],'q4':['march','Q4']}
def qMatch(Q,nlText):
    for q in quarter[Q]:
        if q.lower() in nlText.lower():
            return True
        else:
            return False



def yearFormat(year):
    year='20'+year
    year=re.sub('_','-',year)
    return year

def FYQ(year,Q):
    for x in res_n[0].xpath("//div[@class='container-fluid mt-4 mb-0 my-md-5 ']//div[@class='table-paginantion-comp aem-GridColumn aem-GridColumn--default--12']//div[@class='page-description aem-GridColumn aem-GridColumn--default--12']//tbody"):
        yearText=x.xpath(".//th//text()").extract()[0]
        print(yearText)
        for link in x.xpath(".//td//a"):
            nlLink=link.xpath(".//@href").extract()[0]
            nlText=link.xpath(".//text()").extract()[0]
            print(nlText)
            if qMatch(Q,nlText) and yearFormat(year) in yearText:
                nlLink=domain+nlLink
                data=requests.get(nlLink,headers=headers)
                print(data)
                p=os.path.join('output', "iffco_"+year+"_"+Q+".pdf")
                open(p, 'wb').write(data.content)
        
    
FYQ('22_23','q2')


        