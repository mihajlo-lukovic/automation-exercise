from pages import Pages


def test_contact_us_submission(driver, mock_data):
    """Contact us Form – Successful Submission

    Preconditions:
    - User is on the “Contact us” page
    - Test Data:
        1. Name: text
        2. Email: valid email format
        3. Subject: text
        4. Message: text


    Test steps:
    1. In the section “Get in Touch” fill in “Name”, "Email", “Subject” and
    “Message” fields -> Fields accepts valid test data
    2. Click “Submit” button -> JavaScript alert is displayed
    3. Click on “OK” button to proceed -> Message
    "Success! Your details have been submitted successfully." is displayed
    """
    pages = Pages(driver=driver)

    # User is on the “Contact us” page
    pages.home.navigate()
    pages.home.contact_us.wait_and_click()

    # 1. In the section “Get in Touch” fill in “Name”, "Email", “Subject” and
    # “Message” fields -> Fields accepts valid test data
    # 2. Click “Submit” button -> JavaScript alert is displayed
    pages.contact_us.submit_contact_form(
        name=mock_data['name'],
        email=mock_data['email'],
        subject=mock_data['subject'],
        description=mock_data['description']
    )

    pages.contact_us.accept_js_alert()

    # 3. Click on “OK” button to proceed -> Message
    # "Success! Your details have been submitted successfully." is displayed
    pages.contact_us.contact_us_message.wait_to_be_displayed()
    assert (
            pages.contact_us.contact_us_message.text() ==
            'Success! Your details have been submitted successfully.'
    ), 'Contact us message is incorrect'
