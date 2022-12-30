from importlib.resources import path
from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.selector import Selector
import re
import os
from playwright.async_api import async_playwright
import asyncio
url="https://www.careinsurance.com/public-disclosures.html"
domain="https://www.careinsurance.com"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
res=requests.get(url,headers=headers)

response=Selector(res)
res_n=response.css('body')

year=['2021-22','2022-23']

quarter={'q1':'1st Quarter','q2':'2nd Quarter','q3':'3rd Quarter','q4':'4th Quarter'}


async def run(FY):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        print(FY)
        # Click text=FY 21-22
        await page.frame_locator("#iFrameResizer0").locator("text=FY "+FY).click()
        # await page.frame_locator("#iFrameResizer0").locator("text=Qtr 1 22-23").click()
        
        return await page.content()




def yearFormat(year):
    year=re.sub('_','-',year)
    return year

def FYQ(year,Q):
    
    data=asyncio.run(run(yearFormat(year)))
    # print(data)

    if data==None:
        return
    soup=BeautifulSoup(data,'lxml')
    # x=soup.find('div',class_='brochureOuter')
    x=soup.find_all('a')
    for i in x:
        nlText=i.text
        if nlText!=None:
            
            if '.pdf' in nlText:
                print(nlText)


        # qText=x.xpath(".//div[@class='leftotherbox']//div[@class='jss297 jss1040 jss1010 jss1014']")
        # print(qText)
        
    

FYQ('21_22','q2')


        