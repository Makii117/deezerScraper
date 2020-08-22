from selenium import webdriver
from bs4 import BeautifulSoup as soup
import sys
from urllib.request import Request, urlopen
import urllib.request
from lxml import html,etree

print("-"*50)
print("Input artist url")
print("Example: https://www.deezer.com/en/artist/10159994")
print("-"*50)
try:
    #url=str(input("Artist url: "))
    url="https://www.deezer.com/en/artist/10159994"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    req = Request(url, headers=headers)
    page = urlopen(req).read()
    scraped=soup(page,'lxml')
    dom = etree.HTML(str(scraped))
    #div1=scraped.find("div",{"id":"dzr-app"})
    #for child in div1.descendants:
        #print(child)
    heh=dom.xpath(//*[@id="page_naboo_artist"]/div[2]/div/div[2]/div/ul[1])          
    print(heh)

except KeyboardInterrupt:
    print("Keyboard Intterupt, Exiting")
    sys.exit()