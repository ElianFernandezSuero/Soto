from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        # Inventory page locators
        self.burger_menu = (By.ID, "react-burger-menu-btn")
        self.logout_button = (By.ID, "logout_sidebar_link")

    def open_burger_menu(self):
        self.driver.find_element(*self.burger_menu).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()
