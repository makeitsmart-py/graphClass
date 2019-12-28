from libs.vk_ui_interface.base import BaseVkPage
from libs.vk_ui_interface.elements import *
from libs.vk_ui_interface.left_menu import LeftMenu
from libs.vk_ui_interface.up_menu import UpMenu


class BaseVkAuthorisedPage(BaseVkPage):
    """Страница ВК после авторизации"""
    leftmenu: 'LeftMenu' = LeftMenu
    upmenu: 'UpMenu' = UpMenu



class FeedPage(BaseVkAuthorisedPage):
    page_path = '/feed'


class MainPage(BaseVkAuthorisedPage):
    page_path = '/id569100170'
    write_post = MainPagePostArea
    publish_post = MainPagePostArea


# Страницы левого меню
class NewsPage(BaseVkAuthorisedPage):
    page_path = '/feed'
    #
    # news = NewsPageNewsButton
    # recommended = NewsPageRecommendedButton
    # search = NewsPageSearchButton
    # likes = NewsPageLikesButton
    # updates = NewsPageUpdatesButton
    # comments = NewsPageCommentsButton


class MessagesPage(BaseVkAuthorisedPage):
    page_path = '/audios569100170'


class FriendsPage(BaseVkAuthorisedPage):
    page_path = '/im'


class GroupsPage(BaseVkAuthorisedPage):
    page_path = '/groups'


class PhotosPage(BaseVkAuthorisedPage):
    page_path = '/albums569100170'


class MusicPage(BaseVkAuthorisedPage):
    page_path = '/audios569100170'


class VideosPage(BaseVkAuthorisedPage):
    page_path = '/video'


class MarksPage(BaseVkAuthorisedPage):
    page_path = '/bookmarks'


# Кнопка логина
class LandingPageLoginButton(NavigateButton):
    _locator = "//*[@id='index_login_button']"
    _next_element = FeedPage

    def click(self) -> FeedPage:
        return super().click()


# Страницы управления профилем из верхнего меню
# class UserProfileEditPage(BaseVkAuthorisedPage):
#     page_path = '/edit'
#
#
# class UserProfileSettingsPage(BaseVkAuthorisedPage):
#     page_path = '/settings'
#
#
# class UserProfileHelpPage(BaseVkAuthorisedPage):
#     page_path = '/support?act=home'
#
#
# class UserProfileLogoutPage(BaseVkAuthorisedPage):
#     page_path = '/'
#
#
# # Страницы Новостей
# class NewsPhotoPage(BaseVkAuthorisedPage):
#     page_path = '/feed?section=photos'
#
#
# class NewsVideoPage(BaseVkAuthorisedPage):
#     page_path = '/feed?section=videos'
#
#
# class NewsFriendsPage(BaseVkAuthorisedPage):
#     page_path = '/feed?section=friends'
#
#
# class NewsGroupsPage(BaseVkAuthorisedPage):
#     page_path = '/feed?section=groups'
#
#
# class NewsPodcastsPage(BaseVkAuthorisedPage):
#     page_path = '/feed?section=podcasts'


# Страница авторизации
class LandingPage(BaseVkPage):
    page_path = '/'
    username = LandingPageUserName
    password = LandingPageUserPassword
    submit = LandingPageLoginButton

