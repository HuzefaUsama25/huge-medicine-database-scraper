from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()

chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
#chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.javascript": 2})
chrome_options.add_argument('--headless')

with open("links.txt","r") as f:
    links = f.read()


links = links.split("\n")



lenlinks = len(links)
count = 0


browser = webdriver.Chrome(options=chrome_options)
browser.implicitly_wait(2)

with open("x.csv","ab+") as f:
    f.write(bytes("Drug Name,Composition,Manufacturer,MRP,Price,Packaging,Prescription,RelatedLabTest,Refrences,ManufacturerAddress\n",encoding="UTF-8"))
    for i in links:
        browser.get(i)
        time.sleep(1)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        try:
            DrugName = browser.find_element_by_css_selector("h1.DrugHeader__title___1NKLq").text.replace(",","").replace("\n","")
        except:
            DrugName = "Drug Name not mentioned"
        try:
            Composition = browser.find_element_by_css_selector("div.saltInfo.DrugHeader__meta-value___vqYM0").text.replace(",","").replace("\n","")
        except:
            Composition = "Composition not mentioned"
            
        try:
            Manufacturer = browser.find_element_by_css_selector("div.DrugHeader__meta-value___vqYM0").text.replace(",","").replace("\n","")
        except:
            Manufacturer = "Manufacturer not mentioned"
            
        try:
            MRP = browser.find_element_by_css_selector("span.DrugPriceBox__bestprice-slashed-price___2ANwD").text.replace(",","").replace("\n","").replace("₹","")
        except:
            MRP = "Not For Sale"
            
        try:
            Price = browser.find_element_by_css_selector("div.DrugPriceBox__best-price___32JXw").text.replace(",","").replace("\n","").replace("₹","")
        except:
            Price = "Not For Sale"
            
        try:
            Packaging = browser.find_element_by_css_selector("div.DrugPriceBox__quantity___2LGBX").text.replace(",","").replace("\n","")
        except:
            Packaging = "Packaging not mentioned"
            
        try:
            Prescription = browser.find_element_by_css_selector("div.DrugHeader__prescription-req___34WVy").text.replace(",","").replace("\n","")
        except:
            Prescription = "Not Mentioned"
            
        try:
            RelatedLabTest = browser.find_element_by_css_selector("div.RelatedLabTests__container___2w3zf").text.replace(",","").replace("\n","")
        except:
            RelatedLabTest = "Not mentioned"
            
        try:
            References = browser.find_element_by_css_selector("div#reference-GA").text.replace(",","").replace("\n","")
        except:
            References = "Not mentioned"
            
        try:
            ManufacturerAddress = browser.find_element_by_css_selector("div.DrugPage__manufacturer-address___2ACya").text.replace(",","").replace("\n","")
        except:
            ManufacturerAddres = "Not mentioned"
            
##        try:
##            ImagePath = browser.find_element_by_css_selector("img.style__image___Ny-Sa.style__loaded___22epL").get_attribute("src").replace(",","").replace("\n","")
##        except:
##            ImagePath = "Image not found!"
         
        print(f"Percentage: {str((count/lenlinks)*100)[0:6]} | Count: {count} | total: {lenlinks}")
        count = count + 1
        f.write(bytes(f"{DrugName},{Composition},{Manufacturer},{MRP},{Price},{Packaging},{Prescription},{RelatedLabTest},{References},{ManufacturerAddress}\n",encoding="UTF-8"))
    #browser.quit()
    f.close()
