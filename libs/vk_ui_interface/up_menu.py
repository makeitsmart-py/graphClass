from libs.ui_interface.base import BaseContainerElement, FwdReference
from libs.ui_interface.elements import *
from selenium.webdriver.common.by import By


class SearchArea(Input):
    _locator = "//*[@id='ts_input']"


class HomeButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/feed')]"
    next = FwdReference('MainPage')


class Notification(BaseContainerElement):
    pass


class UserProfileHomeButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/id569100170')]"
    next = FwdReference('MainPage')


class UserProfileEditButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/edit')]"
    next = FwdReference('UserProfileEditPage')


class UserProfileSettingsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/settings')]"
    next = FwdReference('UserProfileSettingsPage')


class UserProfileHelpButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/support?act=home')]"
    next = FwdReference('UserProfileHelpPage')


class UserProfileLogoutButton(NavigateButton):
    _locator = "//*[@id='top_logout_link']"
    next = FwdReference('UserProfileLogoutPage')


class UserProfile(BaseContainerElement):
    home = UserProfileHomeButton
    edit = UserProfileEditButton
    options = UserProfileSettingsButton
    help = UserProfileHelpButton
    logout = UserProfileLogoutButton


class UserProfileButton(NavigateButton):
    _locator = "//*[@id='top_profile_link']"
    next = UserProfile

    def click(self) -> UserProfile:
        return super().click()


class UpMenu(BaseContainerElement):
    home = HomeButton
    search = SearchArea
    notifications = Notification
    user_profile = UserProfileButton
