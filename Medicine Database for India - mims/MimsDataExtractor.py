import time
import random
import concurrent.futures
from lxml import html
import requests
import traceback
import urllib


with open("links.txt","r") as f:
    links = f.read()
links = links.split("\n")

lenlinks = len(links)
count = 0


#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME

f = open("Brand.csv","w")
f.write(f"Name,Manufacturer,Contentents,CIMS Class,ATC Classification,Form,Packaging/Price\n")
f.close()

f = open("Generic.csv","w")
f.write(f"Name,Dosage,Admin,Contraindications,Special Precautions,Adverse Reactions,Overdose,Drug Intereactions,Action,Storage,CIMS Class,ATC Classification\n")
f.close()



#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "en-US,en;q=0.9", 
    "Dnt": "1", 
    "Sec-Fetch-Dest": "document", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36", 
  }


def scrape(i):
    r = requests.get(i, headers=headers, timeout=(100, 100))
    browser = html.fromstring(r.content)
    try:
        with open("Brand.csv","ab+") as f:
            try:
                Name = browser.xpath('/html/body/div[3]/div[2]/div/div/h1/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                Name = "Not Mentioned"
            try:
                Manu = browser.xpath('/html/body/div[3]/div[2]/div[1]/div[3]/h5/a/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                Manu = "Not Mentioned"
            try:
                Content = browser.xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[2]/div[2]/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                Content = "Not Mentioned"
            try:
                Cims = browser.xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[3]/div[2]/a/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                Cims = "Not Mentioned"
            try:
                Atc = browser.xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[4]/div[2]/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                Atc = "Not Mentioned"
            try:
                Form = browser.xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[5]/div[2]/div[1]/div/div/div/div[2]/span/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                Form = "Not Mentioned"
            try:
                PP = browser.xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[5]/div[2]/div[1]/div/div/div/div[4]/span/text()')[0].replace(",","").replace("\n","").replace("\r","")
            except Exception as e:
                print(e)
                PP = "Not Mentioned"
                
            f.write(bytes(f"{Name},{Manu},{Content},{Cims},{Atc},{Form},{PP}\n", encoding="UTF-8"))
            print(f"33333333333333333333333333333333333333333333333333333333333333333333333333")
            #print("Done")
        
    except Exception as e:
        print(e)


with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
    executor.map(scrape, links)