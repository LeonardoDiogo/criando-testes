
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestCT01:
    def test_ct01_adicionar_produto_carrinho(self):
        driver = conftest.driver
        # Fazendo login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # adicionando a mochila ao carrinho
        driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        # Verificando que a mochila foi adicionada
        driver.find_element(
            By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

        # Clicando para voltar para a tela de produtos
        driver.find_element(By.ID, "continue-shopping").click()
        driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").click()
        driver.find_element(By.XPATH, "//*[text()='Add to cart']").click()

        driver.find_element(
            By.XPATH, "//*[@class='shopping_cart_link']").click()
        assert driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()
        assert driver.find_element(
            By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Bike Light']").is_displayed()
