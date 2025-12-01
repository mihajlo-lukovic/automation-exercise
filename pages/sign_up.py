from framework.actions import BasePage
from framework.elements import Button, Input, Select


class SignUp(BasePage):

    title = Button('css=.radio-inline')
    password = Input('css=input[data-qa="password"]')
    birth_day = Select('css=select[data-qa="days"]')
    birth_month = Select('css=select[data-qa="months"]')
    birth_year = Select('css=select[data-qa="years"]')
    newsletter = Button('css=label[for="newsletter"]')
    special_offer = Button('css=label[for="optin"]')
    first_name = Input('css=input[data-qa="first_name"]')
    last_name = Input('css=input[data-qa="last_name"]')
    address = Input('css=input[data-qa="address"]')
    country = Select('css=select[data-qa="country"]')
    state = Input('css=input[data-qa="state"]')
    city = Input('css=input[data-qa="city"]')
    zipcode = Input('css=input[data-qa="zipcode"]')
    mobile_number = Input('css=input[data-qa="mobile_number"]')
    create_account = Button('css=button[data-qa="create-account"]')

    def select_title(self, title: str):
        self.title.wait_to_be_displayed()
        title_options = self.find_elements_by_locator(self.title.locator)

        for title_option in title_options:
            if title in title_option.text:
                title_option.click()
                break
        else:
            raise ValueError(f'Title option {title} not found')

    def complete_sign_up_form(
            self,
            title: str,
            password: str,
            birth_day: int,
            birth_month: str,
            birth_year: str,
            first_name: str,
            last_name: str,
            address: str,
            country: str,
            state: str,
            city: str,
            zipcode: str,
            mobile_number: str
    ):
        # Select title based on title text
        self.title.wait_to_be_displayed()
        self.select_title(title=title)

        self.password.type(password)

        # Add birth information
        self.birth_day.select_by_text(birth_day)
        self.birth_month.select_by_text(birth_month)
        self.birth_year.select_by_text(birth_year)

        # Check newsletter and special offer checkboxes
        self.newsletter.wait_and_click()
        self.special_offer.wait_and_click()

        # Add basic information
        self.first_name.type(first_name)
        self.last_name.type(last_name)

        # Add living and contact details
        self.address.type(address)
        self.country.select_by_text(country)
        self.state.type(state)
        self.city.type(city)
        self.zipcode.type(zipcode)
        self.mobile_number.type(mobile_number)

        # Click on the Create account button
        self.create_account.wait_and_click()
