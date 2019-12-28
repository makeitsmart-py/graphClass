from libs.ui_interface.base import BasePage
from .base import BaseContainerElement, BaseElement, BasePage, __DEFAULT__
from selenium.webdriver.common.keys import Keys
import typing


class Button(BaseElement):

    def click(self):
        el = self._wait_element()
        el.click()


# scope chain
class NavigateButton(Button):
    _next_element: typing.Union[typing.Type[BasePage], typing.Type[BaseElement]] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self._next_element is None:
            raise ValueError(f"{self.__class__} NavigateButton requires _next_element to be defined")
        if isinstance(self._next_element, type):
            if not issubclass(self._next_element, (BasePage, BaseElement)):
                raise ValueError(f"{self.__class__} NavigateButton _next_element could be PageClass or BaseElement instance")
        elif not isinstance(self._next_element, BaseElement):
            raise ValueError(f"{self.__class__} NavigateButton _next_element could be PageClass or BaseElement instance")

    def click(self):
        super().click()
        if isinstance(self._next_element, type):
            if issubclass(self._next_element, BasePage):
                next_element = self._next_element(self._get_page().driver)
            elif issubclass(self._next_element, BaseElement):
                next_element = self._next_element()
                next_element = next_element._instantiate(self._get_page(), parent_container=self._get_page())
        elif isinstance(self._next_element, BaseElement):
            next_element = self._next_element._instantiate(self._get_page(), parent_container=self._get_page())
        next_element.wait_till_is_visible()
        return next_element


class Input(BaseElement):
    value = None

    def set_text(self, value):
        el = self._wait_element()
        el.send_keys(value)

    def get_text(self):
        if self.value is not None:
            return self.value

    def submit(self):
        el = self._wait_element()
        el.send_keys(Keys.RETURN)


class SecuredInput(Input):
    pass


class InteractiveInput(Input):
    pass


class Label(BaseElement):
    pass


class CheckBox(BaseElement):
    def change(self):
        pass


class PopupContainerButton(Button):
    _next_container: typing.Type[BaseContainerElement] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self._next_container is None:
            raise ValueError(f"{self.__class__} PopupContainerButton requires _next_container to be defined")

    def click(self):
        super().click()
        next_container = self._next_container(self._get_page().driver)
        next_container.wait_till_is_loaded()
        return next_container

