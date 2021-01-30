from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
ask_num=int(input("Enter number of time to spam the message: "))
ask_text = input("Enter the message you wanna spam: ")
ask_contact=input("Enter contact's name: ")
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(ask_contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+ask_contact+"']")
selected_contact.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
for i in range(ask_num):
    input_box.send_keys(ask_text + Keys.ENTER)
time.sleep(2)
driver.quit()