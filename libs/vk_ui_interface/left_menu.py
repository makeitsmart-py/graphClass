from libs.ui_interface.base import BaseContainerElement, FwdReference
from libs.ui_interface.elements import NavigateButton
from selenium.webdriver.common.by import By


class HomeButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/id569100170')]"
    _next_element = FwdReference('MainPage')
    

class NewsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/feed')]"
    _next_element = FwdReference('NewsPage')


class MessagesButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/im')]"
    _next_element = FwdReference('MessagesPage')
    
    
class FriendsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/friends')]"
    _next_element = FwdReference('FriendsPage')


class GroupsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/groups')]"
    _next_element = FwdReference('GroupsPage')
    

class PhotosButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/albums')]"
    _next_element = FwdReference('PhotosPage')
    

class MusicButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/audios')]"
    _next_element = FwdReference('MusicPage')


class VideosButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/video')]"
    _next_element = FwdReference('VideosPage')
    

class MarksButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/bookmarks')]"
    _next_element = FwdReference('MarksPage')
    
    
class LeftMenu(BaseContainerElement):
    _locator = "//*[@id='side_bar']"
    music = MusicButton
    news = NewsButton
    messages = MessagesButton
    friends = FriendsButton
    groups = GroupsButton
    photos = PhotosButton
    videos = VideosButton
    marks = MarksButton
    my = HomeButton
