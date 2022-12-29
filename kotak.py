from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os

url="https://www.kotakgeneral.com/public-disclosure"
domain="https://www.kotakgeneral.com"

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
    print(Q)
    for x in res_n[0].xpath("//div[@class='disclouser_container']//div[@class='iconTabs-content']//div[@class='quarter2']"):#//div[@class='col-ssm-12 col-xs-6 col-md-4 pad-bt-15']"): #//div[@id='col-md-12 col-sm-12 col-xs-12 pad-l-r-0 ng-star-inserted']
        print(x)
    

FYQ('22_23','q2')


        