from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

ruta = os.path.abspath("login.html")
driver.save_screenshot("screenshots/login_correcto.png")

driver.get("file:///" + ruta.replace("\\", "/"))

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.ID, "login").click()

time.sleep(5)

driver.find_element(By.ID, "nombre").send_keys("Producto 1")
driver.find_element(By.ID, "guardar").click()
driver.save_screenshot("screenshots/crear.png")

driver.find_element(By.ID, "nombre").clear()
driver.find_element(By.ID, "guardar").click()

time.sleep(2)

alert = driver.switch_to.alert
alert.accept()

driver.save_screenshot("screenshots/limite.png")

time.sleep(5)

driver.find_element(By.XPATH, "//button[contains(text(),'Editar')]").click()

time.sleep(3)

alert = driver.switch_to.alert
alert.send_keys("Producto Editado")
alert.accept()
driver.save_screenshot("screenshots/editar.png")

time.sleep(3)

driver.find_element(By.XPATH, "//button[contains(text(),'Eliminar')]").click()
driver.save_screenshot("screenshots/eliminar.png")

time.sleep(3)

driver.get("file:///" + ruta.replace("\\", "/"))

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("wrong")
driver.find_element(By.ID, "login").click()

time.sleep(2)

alert = driver.switch_to.alert
alert.accept()

driver.save_screenshot("screenshots/login_incorrecto.png")