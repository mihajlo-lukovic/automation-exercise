from framework.actions import TIMEOUT


class Element(object):

    def __init__(self, locator, page=None):
        self.locator = locator
        self.page = page

    def __get__(self, obj, type_c=None):
        if obj is None:
            return self
        return self.__class__(self.locator, obj)

    def wait_to_be_displayed(self, timeout=TIMEOUT, message=None):
        return self.page.wait_to_be_displayed(self.locator, timeout, message)

    def text(self, timeout=TIMEOUT):
        return self.page.text(self.locator, timeout)

    def attribute_text(self, attribute, timeout=TIMEOUT):
        return self.page.attribute_text(self.locator, attribute, timeout)


class Input(Element):

    def type(self, keys, clear=False):
        self.page.type(self.locator, keys, clear)


class Button(Element):

    def wait_and_click(self, timeout=TIMEOUT, message=None):
        self.page.wait_and_click(self.locator, timeout, message)


class Select(Element):

    def select_by_text(self, option: str):
        self.page.select_by_text(self.locator, option)
