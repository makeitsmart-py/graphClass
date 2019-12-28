from libs.ui_interface.base import BaseContainerElement, FwdReference
from libs.ui_interface.elements import *
from selenium.webdriver.common.by import By


class SearchArea(Input):
    _locator = "//*[@id='ts_input']"


class HomeButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/feed')]"
    _next_element = FwdReference('MainPage')


class Notification(BaseContainerElement):
    pass


class UserProfileHomeButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/id569100170')]"
    _next_element = FwdReference('MainPage')


class UserProfileEditButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/edit')]"
    _next_element = FwdReference('UserProfileEditPage')


class UserProfileSettingsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/settings')]"
    _next_element = FwdReference('UserProfileSettingsPage')


class UserProfileHelpButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/support?act=home')]"
    _next_element = FwdReference('UserProfileHelpPage')


class UserProfileLogoutButton(NavigateButton):
    _locator = "//*[@id='top_logout_link']"
    _next_element = FwdReference('UserProfileLogoutPage')


class UserProfile(BaseContainerElement):
    home = UserProfileHomeButton
    edit = UserProfileEditButton
    options = UserProfileSettingsButton
    help = UserProfileHelpButton
    logout = UserProfileLogoutButton


class UserProfileButton(NavigateButton):
    _locator = "//*[@id='top_profile_link']"
    _next_element = UserProfile

    def click(self) -> UserProfile:
        return super().click()


class UpMenu(BaseContainerElement):
    home = HomeButton
    search = SearchArea
    notifications = Notification
    user_profile = UserProfileButton
