from libs.ui_interface.base import BaseContainerElement, FwdReference
from libs.ui_interface.elements import *
from selenium.webdriver.common.by import By


# Элементы на страннице логина
class LandingPageUserName(Input):
    _locator = "//*[@id='index_email']"


class LandingPageUserPassword(SecuredInput):
    _locator = "//*[@id='index_pass']"


class MainPagePostArea(Input):
    _locator = "//*[@id='post_field']"


class MainPageSendPostButton(Button):
    _locator = "//*[@id='send_post']"


# Элементы во вкладке Новости

# class NewsPhotoButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_photos")
#     _next_element = FwdReference('NewsPhotoPage')
#
#
# class NewsVideoButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_videos")
#     _next_element = FwdReference('NewsVideoPage')
#
#
# class NewsGroupsButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_groups")
#     _next_element = FwdReference('NewsGroupsPage')
#
#
# class NewsFriendsButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_friends")
#     _next_element = FwdReference('NewsFriendsPage')
#
#
# class NewsPodcastsButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_podcasts")
#     _next_element = FwdReference('NewsPodcastsPage')
#
#
# class News(BaseContainerElement):
#     photo = NewsPhotoButton
#     video = NewsVideoButton
#     groups = NewsGroupsButton
#     friends = NewsFriendsButton
#     podcasts = NewsPodcastsButton
#
#
# class NewsPageNewsButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_news")
#     _next_element = News
#
#     def click(self) -> News:
#         return super().click()
#
#
# class NewsPageRecommendedButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_recommended")
#
#
# class NewsPageSearchButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_search")
#
#
# class NewsPageLikesButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_likes")
#
#
# class NewsPageUpdatesButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_updates")
#
#
# class NewsPageCommentsButton(NavigateButton):
#     _locator = (By.ID, "ui_rmenu_comments")


