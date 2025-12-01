import time

from framework.actions import BasePage
from framework.elements import Element, Button, Input


class ProductDetails(BasePage):

    # Product details
    product_name = Element('css=.product-information h2')
    add_to_cart = Button('css=.cart')

    # Product review
    review_name = Input('css=input#name')
    review_email = Input('css=input#email')
    review_description = Input('css=textarea#review')
    review_submit = Button('id=button-review')
    review_message = Element('css=div#review-section')

    # Add to cart modal
    cart_modal = Element('css=.modal-content')
    cart_modal_message = Element('css=.modal-body')
    cart_view = Button("xpath=//div[contains(@class,'modal-content')]//a")

    def get_product_name(self) -> str:
        self.product_name.wait_to_be_displayed()
        return self.product_name.text()

    def add_product_to_cart(self, check_message: bool = True):
        self.add_to_cart.wait_and_click()

        if check_message:
            self.assert_success_cart_modal_message()

    def assert_success_cart_modal_message(self):
        self.cart_modal.wait_to_be_displayed()

        assert (
                self.cart_modal_message.text() ==
                'Your product has been added to cart.\nView Cart'
        ), 'Cart modal message content incorrect'

    def submit_product_review(self, name: str, email: str, description: str):
        self.review_name.wait_to_be_displayed()

        self.review_name.type(name)
        self.review_email.type(email)
        self.review_description.type(description)

        self.review_submit.wait_and_click()

    def wait_for_review_message(self, timeout: int = 5):
        now = time.time()
        while time.time() - now < timeout:
            if 'hide' not in self.review_message.attribute_text('class'):
                break
        else:
            raise AssertionError(
                f'Review message is not displayed in {timeout} seconds'
            )
