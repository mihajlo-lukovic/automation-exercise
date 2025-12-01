from framework.actions import BasePage
from framework.elements import Input, Button, Element


class ContactUs(BasePage):

    name = Input('css=input[data-qa="name"]')
    email = Input('css=input[data-qa="email"]')
    subject = Input('css=input[data-qa="subject"]')
    description = Input('css=textarea[data-qa="message"]')
    submit = Button('css=input[data-qa="submit-button"]')
    contact_us_message = Element('css=.contact-form div.alert-success')

    def submit_contact_form(
            self, name: str, email: str, subject: str, description: str
    ):
        self.name.wait_to_be_displayed()

        self.name.type(name)
        self.email.type(email)
        self.subject.type(subject)
        self.description.type(description)

        self.submit.wait_and_click()
