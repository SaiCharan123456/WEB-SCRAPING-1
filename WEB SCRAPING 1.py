from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    head = ["V Mag. (mV)","Proper name","Bayer designation","Distance (ly)","Spectral class","Mass (M☉)","Radius (R☉)"	,"Luminosity (L☉)"]
    planet_data = []

    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
            td_tags = tr_tag.find_all("td")
            temp_list = []
            print("before a tag")
            for index, td_tag in enumerate(td_tags):
                if index == 1:
                    print("in the a tag")
                    a_tag = td_tag.find_all("a")
                    temp_list.append(a_tag)
                else:
                    try:
                        temp_list.append(td_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            print("after creating list")
            print(head)
            
    with open("web scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(head)
        csvwriter.writerows(planet_data)
    
        
scrape()
#head = ["V Mag. (mV)","Proper name","Bayer designation","Distance (ly)","Spectral class","Mass (M☉)","Radius (R☉)"	,"Luminosity (L☉)"]
#planet = 

