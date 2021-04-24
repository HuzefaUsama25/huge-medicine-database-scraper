from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time


chrome_options = Options()
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.javascript": 2})
chrome_options.add_argument('--headless')

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
f.write(f"Name,Manufacturer,Contentents,CIMS Class,ATC Classification,Form,Quantity1,Price1,Quantity2,Price2")
f.close()

f = open("Generic.csv","w")
f.write(f"")
f.close()

#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME
#REMOVE THIS BEFORE RUNNING SECOND TIME


for i in links:
    browser.get(i)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    check = browser.current_url
    if "generic" in str(check).lower:
        try:
            with open("Brand.csv","ab+") as f:
                full = browser.find_element_by_css_selector("a#FullPrescribingInfo.drug-group-item.color-black ")
                full.click()
                window_after = browser.window_handles[1]
                browser.switch_to.window(window_after)
                Name = browser.find_element_by_css_selector("h1.druginfo-header.text-capitalize.drug-header.no-padding").text.replace(",","").replace("\n","")
                Dosage = browser.find_element_by_xpath('//*[@id="dosage"]/div[2]').text.replace(",","").replace("\n","")
                Admin = browser.find_element_by_xpath('//*[@id="administration"]/div[2]').text.replace(",","").replace("\n","")
                Contradict = browser.find_element_by_xpath('//*[@id="contraindications"]/div[2]').text.replace(",","").replace("\n","")
                Spre = browser.find_element_by_xpath('//*[@id="special-precautions"]/div[2]').text.replace(",","").replace("\n","")
                Arec = browser.find_element_by_xpath('//*[@id="adverse-reactions"]/div[2]').text.replace(",","").replace("\n","")
                Over = browser.find_element_by_xpath('//*[@id="over-dosage"]/div[2]').text.replace(",","").replace("\n","")
                Dint = browser.find_element_by_xpath('//*[@id="drug-interaction"]/div[2]').text.replace(",","").replace("\n","")
                Act = browser.find_element_by_xpath('//*[@id="mechanism-of-action"]/div[2]').text.replace(",","").replace("\n","")
                Store = browser.find_element_by_xpath('//*[@id="storage"]/div[2]').text.replace(",","").replace("\n","")
                Cims = browser.find_element_by_xpath('//*[@id="mims-class"]/div[2]').text.replace(",","").replace("\n","")
                Atc = browser.find_element_by_xpath('//*[@id="atc-class"]/div[2]').text.replace(",","").replace("\n","")
                f.write(bytes(f"{Name},{Dosage},{Admin},{Contradict},{Spre},{Arec},{Over},{Dint},{Act},{Store},{Cims},{Atc}", encoding="UTF-8"))
            
        
        except NoSuchElementException:
            pass
    else:
        try:
            with open("Brand.csv","ab+") as f:
                Name = browser.find_element_by_css_selector("div.div-brand").text.replace(",","").replace("\n","")
                Manu = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/h5/a').text.replace(",","").replace("\n","")
                Content = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[2]/div[2]').text.replace(",","").replace("\n","")
                Cims = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[3]/div[2]/a').text.replace(",","").replace("\n","")
                Atc = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[4]/div[2]').text.replace(",","").replace("\n","")
                Form = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[5]/div[2]/div[1]/div/div/div/div[2]/span').text.replace(",","").replace("\n","")
                PP = browser.find_element_by_xpath('/html/body/div[3]/div[6]/div[1]/div[1]/div/div/div[5]/div[2]/div[1]/div/div/div/div[4]/span').text.replace(",","").replace("\n","")
                PP = PP.split(";")
                First = PP[0]; Sec = PP[1]
                Quan1 = First.split(" ")[1]
                Price1 = First.split(" ")[2]
                Quan2 = Sec.split(" ")[1]
                Price2 = Sec.split(" ")[2]
                f.write(bytes("{Name},{Manu},{Content},{Cims},{Atc},{Form},{Quan1},{Price1},{Quan2},{Price2}\n", encoding="UTF-8"))
            
        except NoSuchElementException:
            pass


    
'''

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
'''
