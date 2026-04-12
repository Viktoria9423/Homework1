from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

# ввод логина
username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

# ввод пароля
password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

# кнопка логина
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

time.sleep(5)

# получение текста
message = driver.find_element(By.ID, "flash").text
print(message)

driver.quit()
