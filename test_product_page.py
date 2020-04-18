from pages.product_page import ProductPage
from pages.product_page import BasePage
import time
import pytest

@pytest.mark.parametrize('offerNum', range(0)) #9
def test_guest_can_add_product_to_basket(browser, offerNum):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer' + str(offerNum)
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.solve_quiz_and_get_code()
    page.if_added_successfully()

@pytest.mark.xfail(reason="works as expected")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    #time.sleep(50)
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="works as expected")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_busket()
    page.should_dissapear_of_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
 
