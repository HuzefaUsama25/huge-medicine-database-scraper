from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.javascript": 2})

browser = webdriver.Chrome(options=chrome_options)

browser.get("https://www.1mg.com/drugs-all-medicines")
time.sleep(10)
print("started")
links = []


alphabets = browser.find_elements_by_css_selector("span.style__label___3RBMm")
nextbutton = browser.find_element_by_css_selector("a.button-text.link-next")



products = browser.find_elements_by_css_selector("a.button-text.style__flex-row___2AKyf.style__flex-1___A_qoj.style__product-name___HASYw")

for alphabet in alphabets:
    alphabet.click()
    products = browser.find_elements_by_css_selector("a.button-text.style__flex-row___2AKyf.style__flex-1___A_qoj.style__product-name___HASYw")
    while True:
        for i in products:
            try:
                link = i.get_attribute("href")
            except:
                continue
            links.append(link)
            f = open("links.txt","a+")
            f.write(link+"\n")
            f.close()
        currenturl = browser.current_url
        nextbutton.click()
        newurl = browser.current_url
        time.sleep(1)
        products = browser.find_elements_by_css_selector("a.button-text.style__flex-row___2AKyf.style__flex-1___A_qoj.style__product-name___HASYw")
        print(len(links))
        if currenturl==newurl:
            print(f"Scraped: {alphabet.text}")
            break   

