from framework.actions import BasePage
from framework.elements import Button


class Home(BasePage):

    products = Button('css=a[href="/products"]')
    video_tutorials = Button('css=a[href*="AutomationExercise"]')
    contact_us = Button('css=a[href="/contact_us"]')
    sign_up_or_login = Button('css=a[href="/login"]')
