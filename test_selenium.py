from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/ac974/OneDrive/Documents/GitHub/Tarea4/login.html")

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "login").click()

time.sleep(3)

driver.quit()