import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_Login(self):
        #step
        browser = self.browser #buka browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("basten.ang@gmail.com") #isi valid email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("bas123") #isi valid pass
        time.sleep(1)
        browser.find_element(By.ID,"sign_in").click() # klik button sign in
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome',response_data)
        self.assertEqual(response_message,'Login Successful')

    def test_b_failed_Login_with_invalid_email(self):
        #step
        browser = self.browser #buka browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("basten.anggoro@gmail.com") #isi invalid email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("bas123") #isi valid pass
        time.sleep(1)
        browser.find_element(By.ID,"sign_in").click() # klik button sign in
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('email and password not found',response_data)
        self.assertEqual(response_message,'Email or password invalid')

    def test_c_failed_Login_with_invalid_password(self):
        #step
        browser = self.browser #buka browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("basten.ang@gmail.com") #isi valid email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("123bas") #isi invalid pass
        time.sleep(1)
        browser.find_element(By.ID,"sign_in").click() # klik button sign in
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('email and password not found',response_data)
        self.assertEqual(response_message,'Email or password invalid')

    def test_d_failed_Login_with_invalid_email_password(self):
        #step
        browser = self.browser #buka browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("basten.anggoro@gmail.com") #isi invalid email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("123bas") #isi invalid pass
        time.sleep(1)
        browser.find_element(By.ID,"sign_in").click() # klik button sign in
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('email and password not found',response_data)
        self.assertEqual(response_message,'Email or password invalid')

     def test_e_failed_Login_with_without_email_password(self):
        #step
        browser = self.browser #buka browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") #empty email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") #empty pass
        time.sleep(1)
        browser.find_element(By.ID,"sign_in").click() # klik button sign in
        time.sleep(1)

        #validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('email and password not found',response_data)
        self.assertEqual(response_message,'Email or password empty')

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()