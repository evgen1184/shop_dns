
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_clases import Base


class Main_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    select_rolls = "//*[@id='link_1']"
    select_product_1 = "//*[@id='cat4']/div/div[1]/div/div[2]/div/button"
    select_product_2 = "//*[@id='cat4']/div/div[2]/div/div[2]/div/button"
    cart = "//*[@id='headerNew']/div/div[13]/div"
    cart_order = "//*[@id='simple-popover']/div[3]/div/div[2]/a/div/button"



    #getters

    def get_select_rolls(self):
        return WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, self.select_rolls)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart_order)))



    # Actions

    def click_select_rolls(self):
        self.get_select_rolls().click()
        print("Click select rolls")
    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product_1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product_2")

    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    def click_cart_order(self):
        self.get_cart_order().click()
        print("Click Cart Order")





    # Methods

    def select_products(self):
        self.get_current_url()
        self.click_select_rolls()
        # self.driver.execute_script("window.scrollTo(0,200)")
        self.click_select_product_1()
        self.click_select_product_2()
        self.click_cart()
        self.click_cart_order()





