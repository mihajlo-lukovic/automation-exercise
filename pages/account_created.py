from framework.actions import BasePage
from framework.elements import Element


class AccountCreated(BasePage):

    account_created_title = Element('css=h2[data-qa="account-created"]')
    account_created_description = Element(
        "xpath=//p[contains(.,'Congratulations! "
        "Your new account has been successfully created!')]"
    )
