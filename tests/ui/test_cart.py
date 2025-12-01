import pytest

from pages import Pages


@pytest.fixture()
def setup(driver):

    pages = Pages(driver=driver)

    # User is on the “Products” page
    pages.home.navigate()
    pages.home.products.wait_and_click()

    # User is on the product details page of any product
    pages.products.view_first_product.wait_and_click()

    yield driver, pages


class TestCart:

    def test_add_to_cart(self, setup):
        """Add Product to Cart

        Preconditions:
        - User is on the “Products” page
        - User is on the product details page of any product

        Test steps:
        1. Click on “Add to cart” button -> Popup shows “Added”
        2. Click on popup's “View Cart” linked text -> Cart page opens with
        the product visible
        """
        driver, pages = setup

        product_name = pages.product_details.get_product_name()

        # 1. Click on “Add to cart” button -> Popup shows “Added”
        pages.product_details.add_product_to_cart()

        # 2. Click on popup's “View Cart” linked text -> Cart page opens with
        # the product visible
        pages.product_details.cart_view.wait_and_click()
        cart_product_name = pages.cart.get_product_name_from_cart(
            product_name=product_name
        )
        assert product_name == cart_product_name, 'Product name incorrect'

    def test_remove_from_cart(self, setup):
        """Delete Product from Cart

        Preconditions:
        - User is on the “Products” page
        - User is on the product details page of any product

        Test steps:
        1. Click on “Add to cart” button -> Popup shows “Added”
        2. Click on popup’s “View Cart” linked text -> Cart page opens with
        the product visible
        3. Click on “X” icon to delete product -> Message
        “Cart is empty! Click here to buy products.” is displayed
        """
        driver, pages = setup

        # 1. Click on “Add to cart” button -> Popup shows “Added”
        pages.product_details.add_product_to_cart()

        # 2. Click on popup’s “View Cart” linked text -> Cart page opens with
        # the product visible
        pages.product_details.cart_view.wait_and_click()

        # 3. Click on “X” icon to delete product -> Message
        # “Cart is empty! Click here to buy products.” is displayed
        pages.cart.cart_item_delete.wait_and_click()
        pages.cart.cart_empty.wait_to_be_displayed()
        assert (
                pages.cart.cart_empty.text() ==
                'Cart is empty! Click here to buy products.'
        ), 'Cart empty message is incorrect'
