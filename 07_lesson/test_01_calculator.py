from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = CalculatorPage(driver)

    page.open()
    page.set_delay("45")

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result()

    driver.quit()

    assert result == "15"
