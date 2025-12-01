from framework.actions import BasePage
from framework.elements import Button, Element, Input


class Products(BasePage):

    products = Element('css=.single-products')
    product_name = Element('css=.productinfo > p')
    view_first_product = Button(
        "xpath=(//div[contains(@class,'choose')]//a)[1]"
    )
    search_product_input = Input('css=input#search_product')
    search_submit = Button('css=button#submit_search')

    def get_product_name(self) -> str:
        first_product = self.find_elements_by_locator(self.products.locator)[0]

        return self.find_element_by_locator(
            parent=first_product,
            locator=self.product_name.locator
        ).text

    def search_product(self, product_name: str):
        self.search_product_input.wait_to_be_displayed()
        self.search_product_input.type(product_name)

        self.search_submit.wait_and_click()
