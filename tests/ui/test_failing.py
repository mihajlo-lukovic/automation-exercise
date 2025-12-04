from pages import Pages


def test_products_title(driver):
    """Test accurate "Products" tab title text

    Preconditions:
        - User is on the “Products” page

    Test steps:
    1. Navigate on the "Products" page -> User is on the "Products" page
    2. Check "Products" tab text -> "Products" tab should have correct text

    Note: Failing test
    """
    pages = Pages(driver=driver)

    # 1. Navigate on the "Products" page -> User is on the "Products" page
    pages.home.navigate()
    pages.home.products.wait_to_be_displayed()

    # 2. Check "Products" tab text -> "Products" tab should have correct text
    assert pages.home.products.text() == 'Test'
