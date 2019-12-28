import unittest
from selenium import webdriver
from libs.vk_ui_interface.pages import *
from libs.ui_interface.elements import *
import time


class VkTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_some_vk(self):

        vk_login_page = LandingPage(self.driver)
        vk_login_page.go_to()
        vk_login_page.username.set_text("+79131198241")
        vk_login_page.password.set_text("gfhjkmfuck")
        vk_feed_page = vk_login_page.submit.click()

        vk_feed_page.leftmenu.my.click()
        # vk_feed_page.write_post.set_text('vasya pidor')
        # vk_feed_page.publish_post.click()






    # def tearDown(self):
    #     self.driver.close()


if __name__ == "__main__":
    unittest.main()