from libs.ui_interface.base import BaseContainerElement, FwdReference
from libs.ui_interface.elements import NavigateButton
from selenium.webdriver.common.by import By


class HomeButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/id569100170')]"
    next = FwdReference('MainPage')
    

class NewsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/feed')]"
    next = FwdReference('NewsPage')


class MessagesButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/im')]"
    next = FwdReference('MessagesPage')
    
    
class FriendsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/friends')]"
    next = FwdReference('FriendsPage')


class GroupsButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/groups')]"
    next = FwdReference('GroupsPage')
    

class PhotosButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/albums')]"
    next = FwdReference('PhotosPage')
    

class MusicButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/audios')]"
    next = FwdReference('MusicPage')


class VideosButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/video')]"
    next = FwdReference('VideosPage')
    

class MarksButton(NavigateButton):
    _locator = "//a[starts-with(@href,'/bookmarks')]"
    next = FwdReference('MarksPage')
    
    
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
