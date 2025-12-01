from framework.actions import BasePage
from framework.elements import Button, Input


class Login(BasePage):

    sign_up_name = Input('css=input[data-qa="signup-name"]')
    sign_up_email = Input('css=input[data-qa="signup-email"]')
    sign_up = Button('css=button[data-qa="signup-button"]')

    def start_sign_up_form(self, name: str, email: str):
        self.sign_up_name.wait_to_be_displayed()

        self.sign_up_name.type(name)
        self.sign_up_email.type(email)

        self.sign_up.wait_and_click()
