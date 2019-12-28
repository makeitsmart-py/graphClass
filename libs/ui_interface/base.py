from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

# import typing


class __DEFAULT__:
    pass


class FwdReference:
    target_class_name = None
    args = None
    kwargs = None
    name = None
    owner = None
    _unresolved_references = {}

    def __init__(self, class_name: str, *args, **kwargs):
        bucket = self._unresolved_references.get(class_name, None)
        if bucket is None:
            bucket = self._unresolved_references[class_name] = []
        bucket.append(self)
        self.target_class_name = class_name
        self.args = args
        self.kwargs = kwargs

    @classmethod
    def resolve(cls, target_class):
        bucket = cls._unresolved_references.get(target_class.__name__, __DEFAULT__)
        if bucket is __DEFAULT__:
            return
        for reference in bucket:
            #instance = target_class(*reference.args, **reference.kwargs)
            if issubclass(reference.owner, BaseContainer):
                reference.owner._elements[reference.name] = target_class
            else:
                setattr(reference.owner, reference.name, target_class)
        del cls._unresolved_references[target_class.__name__]

    def clone(self, new_target_class):
        instance = self.__class__(class_name=self.target_class_name, *self.args, **self.kwargs)
        instance.__set_name__(new_target_class, self.name)
        return instance

    def __get__(self, instance, owner):
        raise RuntimeError(
             f"{self.owner}.{self.name}: Can't resolve forward reference for {self.target_class_name}")

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name


class BaseElement:
    _locator = None
    _name: str = None
    _parent_container: 'BaseContainer' = None
    _page: 'BasePage' = None

    def __init_subclass__(cls, **kwargs):
        FwdReference.resolve(cls)
        super().__init_subclass__(**kwargs)

    def _get_page(self):
        return self._page

    def _wait_element(self, timeout=5):
        if self._locator is None:
            raise ValueError(f"Class '{self.__class__.__name__}' should have 'locator' attribute defined")
        return WebDriverWait(self._page.driver, timeout).until(EC.presence_of_element_located((By.XPATH, self._get_full_xpath())),
                                                               message=f"Can't find element {self._get_full_name()} by locator {self._get_full_xpath()}")

    def _wait_elements(self, timeout=5):
        if self._locator is None:
            raise ValueError(f"Class '{self.__class__.__name__}' should have 'locator' attribute defined")
        return WebDriverWait(self._page.driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, self._get_full_xpath())),
            message=f"Can't find element {self._get_full_name()} by locator {self._get_full_xpath()}")

    def _find_element(self):
        if self._locator is None:
            raise ValueError(f"Class '{self.__class__.__name__}' should have 'locator' attribute defined")
        return self._page.driver.find_element_by_xpath(self._get_full_xpath())

    def _get_full_xpath(self):
        element = self
        full_xpath = []
        while element is not None:
            locator = getattr(element, '_locator', None)
            if locator:
                full_xpath.insert(0, locator)
            element = getattr(element, '_parent_container', None)
        return ''.join(full_xpath)

    def _get_full_name(self):
        element = self
        full_name = []
        while element is not None:
            name = getattr(element, '_name', None)
            if not name:
                name = element.__class__.__name__
            full_name.insert(0, name)
            element = getattr(element, '_parent_container', None)
        return '.'.join(full_name)

    def is_visible(self):
        return not self._is_not_visible()

    def is_not_visible(self):
        return self._is_not_visible()

    def _is_not_visible(self):
        try:
            if self._find_element().is_displayed():
                return False
        except NoSuchElementException:
            return True

    def _instantiate(self, page, parent_container=None, name=None):
        parameters = {}
        for n, v in self.__dict__.items():
            if isinstance(v, (BaseElement, BaseContainer)):
                continue
            parameters[n] = v
        if parent_container is not None:
            parameters['_parent_container'] = parent_container
        parameters['_page'] = page
        instance = self.__class__(**parameters)
        if name:
            instance._name = name
        return instance

    def __init__(self, **kwargs):
        for n, v in kwargs.items():
            if getattr(self.__class__, n, __DEFAULT__) is not __DEFAULT__:
                setattr(self, n, v)
            elif getattr(self.__class__, '_' + n, __DEFAULT__) is not __DEFAULT__:
                setattr(self, '_' + n, v)
            else:
                raise ValueError("%s Unknown __init__ parameter - %s" % (self.__class__, n))


class BaseContainer:
    _elements = None
    _name: str = None

    def __init_subclass__(cls, **kwargs):
        FwdReference.resolve(cls)
        cls._class_get_all_elements()
        super().__init_subclass__(**kwargs)

    @staticmethod
    def _class_get_class_elements(cls, output, remove=False):
        to_delete = []
        for n, v in cls.__dict__.items():
            if (isinstance(v, type) and issubclass(v, (BaseElement, BaseContainer))) or isinstance(v, (
                    BaseElement, BaseContainer, FwdReference)):
                output[n] = v
                if remove:
                    to_delete.append(n)

        if to_delete:
            for n in to_delete:
                delattr(cls, n)

        if cls._elements:
            output.update(cls._elements)

    @classmethod
    def _class_get_all_elements(cls):
        cls._elements = {}
        for subclass in cls.__bases__:
            elements_value = getattr(subclass, '_elements', __DEFAULT__)
            if elements_value is __DEFAULT__:
                continue
            if elements_value is None:
                cls._class_get_class_elements(subclass, cls._elements)
            else:
                cls._elements.update(elements_value)
        for n, v in cls._elements.items():
            if isinstance(v, FwdReference):
                cls._elements[n] = v.clone(cls)
        cls._class_get_class_elements(cls, cls._elements, remove=True)
        return cls._elements

    def __getattr__(self, item):
        element = self._elements.get(item, __DEFAULT__)
        if element is __DEFAULT__:
            raise AttributeError(f"{self.__class__} has no attribute {item}")
        if isinstance(element, type):
            instance = element(page=self._get_page(), parent_container=self, name=item)
            setattr(self, item, instance)
            return instance
        instance = element._instantiate(self._get_page(), parent_container=self, name=item)
        setattr(self, item, instance)
        return instance

    def _get_page(self):
        raise NotImplemented("Abstract method _get_page should be overridden")

    def is_visible(self):
        return not self._is_not_visible()

    def _is_not_visible(self):
        for key in self._elements.keys():
            x = self.__getattr__(key)
            ret = x._is_not_visible()
            if isinstance(ret, str):
                return ret
            if ret:
                return x._get_full_name()
        return False

    def wait_till_is_visible(self, timeout=10):
        end_time = time.time() + timeout
        not_visible_element = None
        while time.time() <= end_time:
            not_visible_element = self._is_not_visible()
            if not not_visible_element:
                return
            time.sleep(1)
        if isinstance(not_visible_element, str):
            raise TimeoutError(f"{self.__class__} element {not_visible_element} is not visible")
        raise TimeoutError(f"{self.__class__} is not visible")

    def _get_full_name(self):
        element = self
        full_name = []
        while element is not None:
            name = getattr(element, '_name', None)
            if not name:
                name = element.__class__.__name__
            full_name.insert(0, name)
            element = getattr(element, '_parent_container', None)
        return '.'.join(full_name)


class BaseContainerElement(BaseElement, BaseContainer):

    def _is_not_visible(self):
        if self._locator is not None:
            if BaseElement._is_not_visible(self):
                return True
        return BaseContainer._is_not_visible(self)


class BasePage(BaseContainer):
    base_url = None
    page_path = None
    title = None

    def __init__(self, driver):
        self.driver = driver

    def _get_title(self):
        return self.driver.title

    def _get_page(self):
        return self

    def go_to(self):
        url = self.get_page_url()
        if url is None:
            raise ValueError("Need url for move")
        self.driver.get(url)

    def get_page_url(self):
        if self.base_url is not None and self.page_path is not None:
            return self.base_url + self.page_path
        return None

    def _is_not_visible(self):
        if self.title is not None:
            if self.title != self._get_title():
                return False
        return super()._is_not_visible()

    # def _find_element(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
    #                                                   message=f"Can't find element by locator {locator}")
    #
    # def _find_elements(self, locator, time=10):
    #     return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
    #                                                   message=f"Can't find elements by locator {locator}")

