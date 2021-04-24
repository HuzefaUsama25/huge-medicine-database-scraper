from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from playsound import playsound
import concurrent.futures

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_argument("start-maximized");
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.javascript": 2})

browser = webdriver.Chrome(options=chrome_options)


browser.get("https://www.mims.com/india/drug")
browser.implicitly_wait(5)


alphabets = []
# Find All Alphabets And store links of each in list Alphabets
abet = browser.find_elements_by_css_selector("div.browse-drugs-box a")
for i in abet:
	alphabets.append(i.get_attribute("href"))


# For Every Alphabet
def scrape(i):
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(i)
    time.sleep(10)
    for x in range(0,1000):
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    links = browser.find_elements_by_css_selector("li#drug-list a")
    for i in links:
        file = open("links.txt","a+")
        file.write(i.get_attribute("href")+"\n")
    file.close()
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(scrape, alphabets)

        
    



