import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("zedamanga")
        driver.find_element(By.ID, "login-button").click()
        assert len(driver.find_elements(
            By.XPATH, "//span[@class='title']")) == 0
