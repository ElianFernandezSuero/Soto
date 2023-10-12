import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..page_objects.inventory_page import InventoryPage
from ..page_objects.login_page import LoginPage


class TestSauceDemoLogin(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.saucedemo.com/")
        cls.driver.implicitly_wait(10)

    def setUp(self):
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        login_page = LoginPage(self.driver)

        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        self.assertIn("inventory", self.driver.current_url)

    def test_logout_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        inventory_page = InventoryPage(self.driver)
        inventory_page.open_burger_menu()
        inventory_page.click_logout_button()

        self.assertIn("www.saucedemo.com", self.driver.current_url)

    def setUp(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.login_page = LoginPage(self.driver)

    def test_invalid_username_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_valid_username_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("invalid_password")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_invalid_username_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_password")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_empty_username_valid_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_valid_username_empty_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_empty_username_empty_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_locked_out_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("locked_out_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue(
            "Epic sadface" in error_message)

    def test_problem_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("problem_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        self.assertIn("inventory", self.driver.current_url)

    def test_performance_glitch_user(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("performance_glitch_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login_button()

        self.assertIn("inventory", self.driver.current_url)

    def test_special_characters_in_credentials(self):
        special_username = "user!@#$%^"
        special_password = "pass!@#$%^"

        login_page = LoginPage(self.driver)
        login_page.enter_username(special_username)
        login_page.enter_password(special_password)
        login_page.click_login_button()

        error_message = login_page.get_error_message()
        self.assertTrue("Epic sadface" in error_message)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
