from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Страница товаров"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def add_backpack(self) -> None:
        """Добавить рюкзак"""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

    def add_tshirt(self) -> None:
        """Добавить футболку"""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    def add_onesie(self) -> None:
        """Добавить комбинезон"""
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

    def go_to_cart(self) -> None:
        """Перейти в корзину"""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
