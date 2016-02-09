import unittest
from selenium import webdriver

class AutomationPracticeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def test_title(self):
        self.driver.get('http://automationpractice.com/index.php')
        self.assertEqual(self.driver.title,'My Store')

    def test_search(self):
        self.driver.get('http://automationpractice.com/index.php')
        search_input = self.driver.find_element_by_css_selector('#search_query_top')
        search_input.send_keys('Blouse')
        search_submit = self.driver.find_element_by_css_selector('#search_block_top .btn.button-search')
        search_submit.click()

    def test_search_result(self):
        self.driver.get('http://automationpractice.com/index.php?controller=search&orderby=position&orderway=desc&search_query=Blouse&submit_search=')
        product = self.assertTrue(self.driver.find_element_by_css_selector('.product_list .product-name'))
        product_blouse = [a.product-name.title for product_name in product]
        self.assertEqual('Blouse', product_blouse)

    def test_add_to_cart_click(self):
        self.driver.get('http://automationpractice.com/index.php')
        add_to_cart_click = self.driver.find_element_by_css_selector('.product-container .button-container')
        add_to_cart_click.click()
        proceed_click = self.driver.find_element_by_css_selector('#layer_cart .layer_cart_cart .button-container .btn')
        proceed_click.click()

    def test_order_summary(self):
        self.driver.get('http://automationpractice.com/index.php?controller=order')
        proceed_checkout_click = self.driver.find_element_by_css_selector('a.button.btn')
        proceed_checkout_click.click()

    def test_order_create_account(self):
        self.driver.get('http://automationpractice.com/index.php?controller=authentication&multi-shipping=0&display_guest_checkout=0&back=http%3A%2F%2Fautomationpractice.com%2Findex.php%3Fcontroller%3Dorder%26step%3D1%26multi-shipping%3D0')
        create_account_input = self.driver.find_element_by_css_selector('input#email_create')
        create_account_input.send_keys('test@test.com')
        create_account_submit = self.driver.find_element_by_css_selector('button#SubmitCreate')
        create_account_submit.click()

    def test_order_sign_in(self):
        self.driver.get('http://automationpractice.com/index.php?controller=authentication&multi-shipping=0&display_guest_checkout=0&back=http%3A%2F%2Fautomationpractice.com%2Findex.php%3Fcontroller%3Dorder%26step%3D1%26multi-shipping%3D0')
        sign_in_email_input = self.driver.find_element_by_css_selector('input#email')
        sign_in_email_input.send_keys('test@test.com')
        sign_in_password_input = self.driver.find_element_by_css_selector('input#passwd')
        sign_in_password_input.send_keys('12345678')
        sign_in_submit = self.driver.find_element_by_css_selector('button#SubmitLogin')
        sign_in_submit.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()