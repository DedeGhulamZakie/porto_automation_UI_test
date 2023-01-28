import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginWebBarru(unittest.TestCase):
   
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_success_login(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        browser.find_element(By.ID,"email").send_keys("dede@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("dede123")
        time.sleep(2)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(2)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(2)

        self.assertIn('Welcome', response_data)
        time.sleep(2)
        self.assertEqual(response_message,'Anda Berhasil Login')
        time.sleep(2)
    
    def test_b_failed_login_with_email_not_registed(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        browser.find_element(By.ID,"email").send_keys("asdasdada@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("dede123")
        time.sleep(2)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(2)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(2)

        self.assertIn('not found', response_data)
        time.sleep(2)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        time.sleep(2)

    def test_c_failed_login_with_email_invalid(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        browser.find_element(By.ID,"email").send_keys("dedemail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("dede123")
        time.sleep(2)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(1)

        email_form = self.browser.find_element(By.ID,"email").get_attribute("validationMessage")
        time.sleep(3)

        self.assertIn('Please include', email_form)
        time.sleep(2)
    
    def test_d_failed_login_with_wrong_password(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        browser.find_element(By.ID,"email").send_keys("dede@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("dede23")
        time.sleep(2)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(2)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(2)

        self.assertIn('not found', response_data)
        time.sleep(2)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        time.sleep(2)
    
    def test_e_failed_login_email_password_empty(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(2)
        browser.find_element(By.ID,"email").send_keys("")
        time.sleep(2)
        browser.find_element(By.ID,"password").send_keys("")
        time.sleep(2)
        browser.find_element(By.ID,"signin_login").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(2)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(2)

        self.assertIn('not found', response_data)
        time.sleep(2)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')
        time.sleep(2)

def tearDown(self): 
    self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

    
