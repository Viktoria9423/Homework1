from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("http://uitestingplayground.com/ajax")


button = driver.find_element(By.ID, "ajaxButton")
button.click()


message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
)

print(message.text)

driver.quit()
