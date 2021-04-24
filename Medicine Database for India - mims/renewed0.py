import requests
from lxml import html
import concurrent.futures
import time
import urllib.request




r = requests.get("https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=https://www.mims.com/india/drug")
tree = html.fromstring(r.content)
alphabets = tree.xpath('/html/body/div[4]/div[3]/div[2]/div/a/@href')
print("Got those Alphabets")
print(f"{len(alphabets)}")

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

def scrape(i):
    print(i)
    url = "https://api.scrapingdog.com/scrape?api_key=5ea541dcacf6581b0b4b4042&url=" + str(i).replace("https","http")
    r = requests.get(url, headers=headers)
    print(f'Got {len(r.content)} bytes')
    tree = html.fromstring(r.content)
    links = tree.xpath('//*[@id="drug-list"]/a/@href')
    print(f"Got {len(links)} links")
    for link in links:
        print("yes")
        with open("links.txt","a+") as f:
            f.write(link+"\n")



with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(scrape, alphabets)