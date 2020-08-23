from bs4 import BeautifulSoup
import sys
from urllib.request import Request, urlopen
import urllib.request
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import lxml
import re
import math
f=open("./deezerScraper/albumUrls.txt",'w')

print("-"*50)
print("Input artist url")
print("Example: https://www.deezer.com/en/artist/10159994")
print("-"*50)


path = r'./deezerScraper/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path = path,chrome_options=options)
albums=[]
li=[]

try:

    url=str(input("Artist url: "))
    
    
    driver.get(url)
    
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
    
    
    ul=driver.find_element_by_xpath('//*[@id="page_naboo_artist"]/div[2]/div/div[2]/div/ul[1]')
    
    
    #print(ul.text)
    for i in range(1,len(ul.find_elements_by_tag_name('li'))):
        
        albumIds=driver.find_element_by_xpath('//*[@id="page_naboo_artist"]/div[2]/div/div[2]/div/ul[1]/li[{}]/div/div[1]/a'.format(i))

    
        print(albumIds.text)
        hrefs=albumIds.get_attribute('href')
        print(hrefs)
        f.write(hrefs+"\n" )




except KeyboardInterrupt:
    print("Keyboard Intterupt, Exiting")
    f.close()
    time.sleep(3)
    sys.exit(0)

except NoSuchElementException:
    print("Thats all, exiting")
    f.close()
    time.sleep(3)
    sys.exit(0)