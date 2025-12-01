from framework.actions import BasePage
from framework.elements import Element, Button


class Cart(BasePage):

    cart_table = Element('css=tbody tr')
    cart_item_name = Element('css=td.cart_description a')
    cart_item_delete = Button('css=.cart_quantity_delete')
    cart_empty = Element('id=empty_cart')

    def get_product_name_from_cart(self, product_name: str):
        for cart_item in self.find_elements_by_locator(
                locator=self.cart_table.locator
        ):
            cart_name = self.find_element_by_locator(
                parent=cart_item,
                locator=self.cart_item_name.locator
            )

            if cart_name.text == product_name:
                return cart_name.text

        raise AssertionError(f'Product with name {product_name} not found')
