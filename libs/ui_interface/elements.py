from .base import BaseContainerElement, BaseElement, BasePage, __DEFAULT__
from selenium.webdriver.common.keys import Keys
import typing


class Button(BaseElement):

    def click(self):
        el = self._wait_element()
        el.click()


class NavigateButton(Button):
    next: typing.Union[typing.Type[BasePage], typing.Type[BaseElement]] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.next is None:
            raise ValueError(f"{self.__class__} NavigateButton requires attribute 'next' to be defined")
        if isinstance(self.next, type):
            if not issubclass(self.next, (BasePage, BaseElement)):
                raise ValueError(f"{self.__class__} NavigateButton attribute 'next' could be PageClass or BaseElement instance")
        elif not isinstance(self.next, BaseElement):
            raise ValueError(f"{self.__class__} NavigateButton attribute 'next' could be PageClass or BaseElement instance")

    def click(self):
        super().click()
        return self._wait_and_instantiate(self.next)


class Input(BaseElement):
    value = None

    def set(self, value, options: dict = None):
        el = self._wait_element()
        el.send_keys(value)

    def get(self):
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

