from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    # логин
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # добавление товаров
    wait.until(EC.visibility_of_element_located((
        By.ID, "add-to-cart-sauce-labs-backpack"
        ))).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # корзина
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # checkout
    driver.find_element(By.ID, "checkout").click()

    # форма
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # итоговая сумма
    total = wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label"
            ))
    ).text

    driver.quit()

    assert total == "Total: $58.29"
