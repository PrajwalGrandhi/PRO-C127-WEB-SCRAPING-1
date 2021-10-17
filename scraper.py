from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests
import pandas as pd

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
time.sleep(10)

star_names=[]
distance=[]
mass=[]
radius=[]
lum=[]
temp_list=[]
page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
star_table=soup.find("table")
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])

df2=pd.DataFrame(list(zip(star_names,distance,mass,radius,lum)),columns=['name','distance','mass','radius',"luminosity"])
df2.to_csv("scraped.csv")
