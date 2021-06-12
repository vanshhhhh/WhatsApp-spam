from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
Chrome_Profile_Path = "user-data-dir=C:\\Users\\vansh\\AppData\\Local\\Google\\Chrome\\User Data\\Wtsp"
options = webdriver.ChromeOptions()
options.add_argument(Chrome_Profile_Path)
def new_chat(user_name):
    new_chat = driver.find_element_by_xpath('//div[@class="ZP8RM"]')
    new_chat.click()
    new_user = driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"]')
    new_user.send_keys(user_name)
    time.sleep(1)
    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()
ask_num=int(input("Enter number of time to spam the message: "))
ask_text = input("Enter the message you wanna spam: ")
ask_contact=str(input("Enter contact's name: "))
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(3)
try:
    user = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath('//span[@title="{}"]'.format(ask_contact)))
    user.click()
except NoSuchElementException as se:
        new_chat(ask_contact)
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
for i in range(ask_num):
    input_box.send_keys(ask_text + Keys.ENTER)
time.sleep(2)
driver.quit()
