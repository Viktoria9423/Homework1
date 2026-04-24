import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Магазин")
@allure.title("Покупка товаров")
@allure.description("Тест проверяет итоговую сумму заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    with allure.step("Открыть сайт"):
        login.open()

    with allure.step("Авторизация"):
        login.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары"):
        inventory.add_backpack()
        inventory.add_tshirt()
        inventory.add_onesie()

    with allure.step("Перейти в корзину"):
        inventory.go_to_cart()

    with allure.step("Оформление заказа"):
        cart.checkout()

    with allure.step("Заполнить форму"):
        checkout.fill_form("Иван", "Петров", "123456")

    with allure.step("Получить итог"):
        total = checkout.get_total()

    driver.quit()

    with allure.step("Проверка суммы"):
        assert total == "Total: $58.29"
