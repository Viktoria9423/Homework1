from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("http://uitestingplayground.com/textinput")


input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")


button = driver.find_element(By.ID, "updatingButton")
button.click()


updated_button = wait.until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)


print(driver.find_element(By.ID, "updatingButton").text)

driver.quit()
