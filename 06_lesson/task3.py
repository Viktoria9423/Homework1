from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 15)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )


images = wait.until(
    lambda driver: driver.find_elements(By.TAG_NAME, "img")
    if len(driver.find_elements(By.TAG_NAME, "img")) >= 3 else False
)


third_image = images[2]

print(third_image.get_attribute("src"))

driver.quit()
