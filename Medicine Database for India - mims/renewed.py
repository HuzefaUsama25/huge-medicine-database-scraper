from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import random
import concurrent.futures


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.javascript": 2})
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--headless')
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")

with open("links.txt","r") as f:
    links = f.read()
links = links.split("\n")

lenlinks = len(links)
count = 0

browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(2)

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


def scrape(i):
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(2)
    browser.get(i)
    browser.implicitly_wait(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    check = browser.current_url
    ran = random.randint(0,1)

    try:
        with open("Brand.csv","ab+") as f:
            browser.implicitly_wait(2)
            try:
                Name = browser.find_element_by_css_selector('/html/body/div[3]/div[2]/div[1]/div[1]/div').text.replace(",","").replace("\n","")
            except:
                Name = "Not Mentioned"
            try:
                Manu = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/h5/a').text.replace(",","").replace("\n","")
            except:
                Manu = "Not Mentioned"
            try:
                Content = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[2]/div[2]').text.replace(",","").replace("\n","")
            except:
                Content = "Not Mentioned"
            try:
                Cims = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[3]/div[2]/a').text.replace(",","").replace("\n","")
            except:
                Cims = "Not Mentioned"
            try:
                Atc = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[4]/div[2]').text.replace(",","").replace("\n","")
            except:
                Atc = "Not Mentioned"
            try:
                Form = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[5]/div[2]/div[1]/div/div/div/div[2]/span').text.replace(",","").replace("\n","")
            except:
                Form = "Not Mentioned"
            try:
                PP = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[5]/div[2]/div[1]/div/div/div/div[4]/span').text.replace(",","").replace("\n","")
            except:
                PP = "Not Mentioned"
                
            f.write(bytes(f"{Name},{Manu},{Content},{Cims},{Atc},{Form},{PP}\n", encoding="UTF-8"))
            #time.sleep(ran)
        
    except:
        pass
    if len(Name) > 1:
        count += 1

    print(f"Percentage: {str(count/lenlinks*100)[:5]} | Done: {count} | Total: {lenlinks}")


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(scrape, links)
    

    
    
    