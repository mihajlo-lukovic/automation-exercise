from pages import Pages


def test_video_tutorials(driver):
    """Navigation to Video Tutorials – External URL

    Preconditions:
    - User is on the “Home” page

    Test steps:
    1. Click on “Video Tutorials” linked text placed at the top of the
    page -> External page displays expected content
    """
    pages = Pages(driver=driver)

    # User is on the “Home” page
    pages.home.navigate()

    # 1. Click on “Video Tutorials” linked text placed at the top of the
    # page -> External page displays expected content
    url = pages.home.video_tutorials.attribute_text('href')
    pages.home.video_tutorials.wait_and_click()
    pages.home.wait_for_url_to_be(url=url)
