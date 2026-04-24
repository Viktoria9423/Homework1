from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Страница калькулятора"""

    def __init__(self, driver: WebDriver) -> None:
        """
        :param driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открыть страницу калькулятора"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value: str) -> None:
        """
        Установить задержку

        :param value: значение задержки
        """
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(value)

    def click_button(self, text: str) -> None:
        """Нажать кнопку калькулятора

        :param text: текст кнопки
        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{text}']"))
        )
        button.click()

    def get_result(self) -> str:
        """Получить результат вычисления

        :return: результат (строка)
        """
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        return self.driver.find_element(By.CLASS_NAME, "screen").text
