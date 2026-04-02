from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

ruta = os.path.abspath("login.html")
driver.get("file:///" + ruta.replace("\\", "/"))

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "login").click()

time.sleep(10)

driver.quit()