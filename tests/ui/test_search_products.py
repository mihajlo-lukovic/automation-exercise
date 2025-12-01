from pages import Pages


def test_single_product_search(driver):
    """Search Product Validation

    Preconditions:
    - User is on the “Products” page
    - User has a valid product keyword for the search

    Test steps:
    1. Enter a valid search keyword in “Search Product” field -> Field
    accepts text
    2. Click on search button -> One or more products matching the keyword
    appear
    """
    pages = Pages(driver=driver)

    # User is on the “Products” page
    pages.home.navigate()
    pages.home.products.wait_and_click()

    # User has a valid product keyword for the search
    pages.products.view_first_product.wait_and_click()
    product_name = pages.product_details.get_product_name()
    pages.home.products.wait_and_click()

    # 1. Enter a valid search keyword in “Search Product” field -> Field
    # accepts text
    # 2. Click on search button -> One or more products matching the keyword
    # appear
    pages.products.search_product(product_name=product_name)
    searched_product_name = pages.products.get_product_name()
    assert (
            product_name == searched_product_name
    ), 'Searched product name is incorrect'
