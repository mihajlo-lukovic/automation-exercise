from pages import Pages


def test_add_product_review(driver, mock_data):
    """Create and Submit Product Review

    Preconditions:
    - User is on the “Products” page
    - User is on the product details page of any product
    - Test Data:
        1. Name: text
        2. Email: valid email format
        3. Review: text

    Test steps:
    1. In the “Write Your Review” section fill in “Your Name”, “Email Address”
    and “Add Review Here!” fields -> Fields accepts valid test data
    2. Click on “Submit” button -> Temporary message
    “Thank you for your review.” is displayed
    """
    pages = Pages(driver=driver)

    # User is on the “Products” page
    pages.home.navigate()
    pages.home.products.wait_and_click()

    # User is on the product details page of any product
    pages.products.view_first_product.wait_and_click()

    # 1. In the “Write Your Review” section fill in “Your Name”,
    # “Email Address” and “Add Review Here!” fields -> Fields accepts valid
    # test data
    # 2. Click on “Submit” button -> Temporary message
    # “Thank you for your review.” is displayed
    pages.product_details.submit_product_review(
        name=mock_data['name'],
        email=mock_data['email'],
        description=mock_data['description']
    )

    pages.product_details.wait_for_review_message()
    assert (
            pages.product_details.review_message.text() ==
            'Thank you for your review.'
    ), 'Review message is incorrect'
