from selenium import webdriver
from time import sleep

driver1 = webdriver.Chrome(executable_path="/Users/pc usr/Downloads/chromedriver")
driver2 = webdriver.Chrome(executable_path="/Users/pc usr/Downloads/chromedriver")
driver3 = webdriver.Chrome(executable_path="/Users/pc usr/Downloads/chromedriver")

driver1.get("link here")
driver2.get("link here")
driver3.get("link here")

while True:
    sleep(60)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()