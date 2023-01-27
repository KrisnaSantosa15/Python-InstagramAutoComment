# Krisna Santosa - Python Scrapping Web - 12 January 2021
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

options = Options()
options.page_load_strategy = 'eager'

# IMPORTANT
komentar = 'Bot test '
jumlah = 8
username = ''  # Isi dengan username IG Kamu
password = ''  # Isi dengan password IG Kamu
login_url = 'https://www.instagram.com/accounts/login/'
comment_url = 'https://www.instagram.com/p/CHo79bCJC0S/'

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(login_url)
# driver.refresh()

time.sleep(3)

driver.find_element_by_xpath(
    '//*[@id="loginForm"]/div[1]/div[5]/button/span[2]').click()
time.sleep(2)

driver.find_element_by_xpath(
    '//*[@id="email"]').send_keys(username)
driver.find_element_by_xpath(
    '//*[@id="pass"]').send_keys(password + Keys.RETURN)

time.sleep(9)
driver.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
driver.get(comment_url)

for i in range(jumlah):
    time.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys(komentar + Keys.RETURN)
    print("comment successfuly Added")
    time.sleep(2)
    driver.refresh()