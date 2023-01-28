import random
import string
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_register(self):
        email_random = ''.join(random.choice(string.ascii_letters) for _ in range(16)) + '@gmail.com'
        name_register = ''.join(random.choice(string.ascii_letters) for _ in range(15))
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys(name_register)
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys(email_random)
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)
    
    def test_b_failed_register_with_empty_name(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("dede24@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(2)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(2)

        self.assertEqual(response_data, 'Oops...')
        time.sleep(2)
        self.assertEqual(response_message,'Gagal Register!')
        time.sleep(2)
    
    def test_c_failed_register_with_empty_email(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("dede")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(1)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(1)

        self.assertEqual(response_data, 'Oops...')
        time.sleep(1)
        self.assertEqual(response_message,'Gagal Register!')
        time.sleep(1)
    
    def test_d_failed_register_with_empty_password(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("dede")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("dede24@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(1)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(1)

        self.assertEqual(response_data, 'Oops...')
        time.sleep(1)
        self.assertEqual(response_message,'Gagal Register!')
        time.sleep(1)
    
    def test_e_failed_register_with_invalid_email(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("dede")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("dede24gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        email_form = self.browser.find_element(By.ID,"email").get_attribute("validationMessage")
        time.sleep(2)

        self.assertIn('Please include', email_form)
        time.sleep(1)  
    
    def test_f_failed_register_name_with_symbol(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("dede!!")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("dede24@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(1)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(1)

        self.assertEqual(response_data, 'Oops...')
        time.sleep(1)
        self.assertEqual(response_message,'Gagal Register!')
        time.sleep(1)
    
    def test_g_failed_register_password_with_symbol(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("dede")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("dede24@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345@@")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)
        
        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(1)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(1)

        self.assertEqual(response_data, 'Oops...')
        time.sleep(1)
        self.assertEqual(response_message,'Gagal Register!')
        time.sleep(1)
    
    def test_h_failed_register_with_email_already_used(self):
        browser = self.browser
        browser.get("https://barru.pythonanywhere.com/daftar")
        time.sleep(5)
        browser.find_element(By.ID,"signUp").click()
        time.sleep(2)
        browser.find_element(By.ID,"name_register").send_keys("dede")
        time.sleep(2)
        browser.find_element(By.ID,"email_register").send_keys("dede24@gmail.com")
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("12345")
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click()
        time.sleep(2)

        response_data = browser.find_element(By.ID,"swal2-title").text
        time.sleep(1)
        response_message = browser.find_element(By.ID,"swal2-content").text
        time.sleep(1)

        self.assertEqual(response_data, 'Oops...')
        time.sleep(1)
        self.assertEqual(response_message,'Gagal Register!')
        time.sleep(1)


def tearDown(self): 
    self.browser.close() 

if __name__ == "__main__": 
    unittest.main()

