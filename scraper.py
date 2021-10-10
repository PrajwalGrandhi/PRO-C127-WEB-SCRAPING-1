from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers=['name','distance','mass','radius']
    stars=[]
    for i in range(0,98):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for tbody in soup.find_all("tbody"):
            tr_tags=tbody.find_all("tr")
            td_tags=tr_tags.find("td")

            temp_list=[]
            for ind,td_tag in enumerate(td_tags):
                if(ind==0):
                    temp_list.append(td_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            stars.append(temp_list)   
    with open("scraped.csv","w") as f:
        csv_writer=csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(stars)
    
scrape()


