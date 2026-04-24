from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Страница корзины"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def checkout(self) -> None:
        """Перейти к оформлению"""
        self.driver.find_element(By.ID, "checkout").click()
