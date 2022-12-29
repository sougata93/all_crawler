from bs4 import BeautifulSoup
import requests
import scrapy
import re
import os
url="https://www.acko.com/public-disclosure/"
res=requests.get(url)
res_=scrapy.selector.Selector(res)
res_n = res_.css("body")

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
    year=re.sub('_','-',year)
    return year


def FYQ(year,Q):

  print(res_n[0])

  for x in res_n[0].xpath(".//div[@class='sc-bdVaJa sc-bwzfXH sc-FQuPU cqunlA']//ul//li//a"):
    text=x.css("::text").extract()[0]
    print(text)
    if yearFormat(year) in text and match(Q,text):
      link=x.xpath("@href").extract()[0]
      data = requests.get(link)
      p=os.path.join('output',"acko_"+year+'_'+Q+'_'+text+".pdf")
      open(p, 'wb').write(data.content)
    #open("acko_"+text+".pdf", 'wb').write(data.content)

FYQ('22_23','q2')