import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Test_success_order(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))   

    def test_success_order(self):
        browser = self.browser
        action = ActionChains(browser)
        browser.maximize_window()

        browser.get("https://magento.softwaretestingboard.com/") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/a").click() #home klik login
        time.sleep(1)
        browser.find_element(By.ID,"email").send_keys("akunml@gmail.com") #fill email
        time.sleep(1)
        browser.find_element(By.ID,"pass").send_keys("Akunml24!") #fill password
        time.sleep(1)
        browser.find_element(By.ID,"send2").click() #click button login
        time.sleep(3)

        response_data = browser.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[1]").text #validasi after login
        self.assertIn('Welcome,', response_data)
        time.sleep(2)


        action.move_to_element(browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]")).perform() #mouseover
        time.sleep(1)
        action.move_to_element(browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a")).perform() #mouseover
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul/li[1]/a").click() #click menu jacket
        time.sleep(1)
        browser.find_element(By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN) #scroll down
        time.sleep(1)
        action.move_to_element(browser.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[5]/div/a/span/span/img")).perform() #mouseover
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[5]/div/a/span/span/img").click() #click product
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div[1]/div[4]/form/div[1]/div/div/div[1]/div/div[2]").click() #choose size
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div[1]/div[4]/form/div[1]/div/div/div[2]/div/div[2]").click() #choose color
        time.sleep(3)
        browser.find_element(By.ID,"product-addtocart-button").click() #click addtocart
        time.sleep(9)
        browser.find_element(By.XPATH,"/html/body/div[2]/header/div[2]/div[1]/a").click() #click basket
        time.sleep(1)
        browser.find_element(By.ID,"top-cart-btn-checkout").click() #click button checkout
        time.sleep(8)
        browser.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div[2]/aside/div[2]/div/div/div[1]/div/div[1]").click() #click order summary
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[1]/div[2]/div[2]/button").click() #click new address
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[3]/div/input").send_keys("blabla") #fill name company
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/fieldset/div/div[1]/div/input").send_keys("lalala") #fill street address
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[4]/div/input").send_keys("blqwdwqabla") #fill city
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[8]/div/select").click() #click dropdownbox country
        time.sleep(1)
        dropdownbox = browser.find_elements(By.TAG_NAME, value="option") #dropdownbox country
        i = 0
        while i < len(dropdownbox):
            if(dropdownbox[i].text == "France"):
                dropdownbox[i].click()
            i = i + 1
        time.sleep(1)
       
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[5]/div/select").click() #click dropdownbox state/province
        time.sleep(1)
        dropdownbox = browser.find_elements(By.TAG_NAME, value="option") #dropdownbox state/province
        i = 0
        while i < len(dropdownbox):
            if(dropdownbox[i].text == "Calvados"):
                dropdownbox[i].click()
            i = i + 1
        time.sleep(1)

        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[7]/div/input").send_keys("12333") #fill zip/postalc ode
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[9]/div/input").send_keys("08987373773") #fill phone number
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/div/div/form/div/div[11]/input").click() #uncheclist save in adrress book
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div[3]/aside[2]/div[2]/footer/button[1]").click() #click ship here
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div[2]/main/div[2]/div/div[2]/div[4]/ol/li[2]/div/div[3]/form/div[3]/div/button").click() #click next
        time.sleep(4)
        browser.find_element(By.XPATH,"/html/body/div[3]/main/div[2]/div/div[2]/div[4]/ol/li[3]/div/form/fieldset/div[1]/div/div/div[2]/div[2]/div[4]/div/button").click() #click place order
        time.sleep(5)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()