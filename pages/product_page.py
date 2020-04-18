from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_busket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)        
        login_link.click() 
    
    def if_added_successfully(self):
        added_text = self.browser.find_element(*ProductPageLocators.ADDING_RESULT).text
        assert added_text == 'Coders at Work', f"{self.browser.current_url}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't dissapear, but had to"


