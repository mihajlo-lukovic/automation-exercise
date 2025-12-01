from pages import Pages


def test_failing_test(driver):
    pages = Pages(driver=driver)

    pages.home.navigate()
    pages.home.products.wait_to_be_displayed()

    assert pages.home.products.text() == 'Test'
