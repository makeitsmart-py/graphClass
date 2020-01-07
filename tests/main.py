import unittest
from selenium import webdriver
from libs.vk_ui_interface.pages import *
from libs.ui_interface.elements import *
import time


class VkTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_some_vk(self):

        vk_login_page = LandingPage(self.driver)
        vk_login_page.go_to()
        vk_login_page.set({
            'username': "+79131198241",
            'password': "gfhjkmfuck"})
        vk_feed_page = vk_login_page.submit.click()
        vk_feed_page.leftmenu.my.click()

    def test_action_chain_vk(self):
        vk_login_page = LandingPage(self.driver)
        vk_feed_page = vk_login_page.ac.go_to().set({
            'username': "+79131198241",
            'password': "gfhjkmfuck"}).submit.click().result
        vk_feed_page.leftmenu.my.click()

    # def tearDown(self):
    #     self.driver.close()


if __name__ == "__main__":
    unittest.main()