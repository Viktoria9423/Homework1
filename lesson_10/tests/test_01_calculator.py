import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Проверка сложения")
@allure.description("Тест проверяет, что 7 + 8 = 15")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    page = CalculatorPage(driver)

    with allure.step("Открыть страницу"):
        page.open()

    with allure.step("Установить задержку"):
        page.set_delay("5")

    with allure.step("Выполнить вычисление"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получить результат"):
        result = page.get_result()

    with allure.step("Проверка результата"):
        assert result == "15"

    driver.quit()
