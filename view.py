from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

driver=webdriver.Chrome('./chromedriver')

driver.get('http://www.naver.com/')

html=driver.page_source

soup=BeautifulSoup(html, 'html.parser')

ranks=soup.select("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k")
print("네이버 검색어 순위")
num=0

while num < 20:
    print(str(num+1)+" "+ranks[num].text)
    num+=1 
