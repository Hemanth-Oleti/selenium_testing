from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


#checking the title
class Hosttest(LiveServerTestCase):
    def testhomepage(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome('./chromedriver', chrome_options=options)

        driver.get(self.live_server_url)
        
        #time.sleep(5)

        assert "Hi" in driver.title

#automating the login

# class LoginFormTest(LiveServerTestCase):
#     def testform(self):

#         driver = webdriver.Chrome()

#         driver.get('http://127.0.0.1:8000/accounts/login')
#         time.sleep(3)

#         user_name = driver.find_element_by_name("username")
#         user_password = driver.find_element_by_name("password")

#         time.sleep(3)

#         submit = driver.find_element_by_id("submit")

#         user_name.send_keys('admin')
#         user_password.send_keys('admin')
        
#         submit.send_keys(Keys.RETURN)

#         assert 'admin' in driver.page_source

