from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Страница оформления заказа"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(
            self, first_name: str, last_name: str, zip_code: str) -> None:
        """
        Заполнить форму

        :param first_name: имя
        :param last_name: фамилия
        :param zip_code: индекс
        """
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Получить итоговую сумму

        :return: строка с суммой
        """
        total = self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total.text
