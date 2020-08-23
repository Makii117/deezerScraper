from bs4 import BeautifulSoup
import sys
from urllib.request import Request, urlopen
import urllib.request
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import lxml
import re
import math

print("-"*50)
print("Input artist url")
print("Example: https://www.deezer.com/en/artist/10159994")
print("-"*50)

path = r'C:\\Users\\BIOSs\\Desktop\\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = path,chrome_options=options)
albums=[]
li=[]

try:

    #url=str(input("Artist url: "))
    url="https://www.deezer.com/en/artist/10159994"
    
    driver.get(url)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',}
    req = Request(url, headers=headers)
    page = urlopen(req).read()
    time.sleep(4)
    #Scroll to bottom of page to get all js loaded
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(0.5)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True
    
    soup=BeautifulSoup(page,'html.parser')
    
    ul=driver.find_element_by_xpath('//*[@id="page_naboo_artist"]/div[2]/div/div[2]/div/ul[1]')
    
    
    print(ul.text)
    for i in range(1,len(li)):
        albumIds=driver.find_element_by_xpath('//*[@id="page_naboo_artist"]/div[2]/div/div[2]/div/ul[1]/li[%s]/div/div[1]/a'%i)

    
        print(albumIds.text)

    



except KeyboardInterrupt:
    print("Keyboard Intterupt, Exiting")
    sys.exit()