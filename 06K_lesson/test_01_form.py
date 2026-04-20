import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

    # заполнение формы
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # zip code НЕ заполняем
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # ожидание результата
    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "danger" in zip_code.get_attribute("class")

    # проверка остальных полей
    fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field in fields:
        element = driver.find_element(By.ID, field)
        assert "success" in element.get_attribute("class")

    driver.quit()
