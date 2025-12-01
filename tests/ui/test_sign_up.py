from pages import Pages


def test_user_sign_up(driver, mock_data):
    """Sign Up Form – Successful Submission

    Preconditions:
    - User is on the “Signup/Login” page
    - User in not logged in
    - Test Data:
        1. Name: text
        2. Email: valid email
        3. All mandatory text fields are populated with valid input
        4. All required radio buttons, select fields, and checkboxes are
        selected/marked as applicable

    Test steps:
    1. Fill in "Name" and "Email Address" in "New User Signup!" -> Fields
    accept valid input
    2. Click on “Signup” button -> Enter Account Information page displays
    the entered "Name" and "Email"
    3. Select "Title", fill "Password", choose "Date of Birth", and check
    both newsletter/offer boxes -> Options are successfully selected
    4. In "Address Information", fill all mandatory fields and select
    "Country" -> Mandatory fields accept input and "Country" is selected
    5. Click on “Create Account” button -> Title “ACCOUNT CREATED!” and
    description “Congratulations! Your new account has been
    successfully created!” are displayed
    """
    pages = Pages(driver=driver)

    # User is on the “Signup/Login” page
    # User in not logged in
    pages.home.navigate()
    pages.home.sign_up_or_login.wait_and_click()

    # 1. Fill in "Name" and "Email Address" in "New User Signup!" -> Fields
    # accept valid input
    # 2. Click on “Signup” button -> Enter Account Information page displays
    # the entered "Name" and "Email"
    pages.login.start_sign_up_form(
        name=mock_data['name'],
        email=mock_data['email']
    )

    # 3. Select "Title", fill "Password", choose "Date of Birth", and check
    # both newsletter/offer boxes -> Options are successfully selected
    # 4. In "Address Information", fill all mandatory fields and select
    # "Country" -> Mandatory fields accept input and "Country" is selected
    # 5. Click on “Create Account” button -> Title “ACCOUNT CREATED!” and
    # description “Congratulations! Your new account has been
    # successfully created!” are displayed
    pages.sign_up.complete_sign_up_form(
        title=mock_data['title'],
        password=mock_data['password'],
        birth_day=mock_data['birth_date'],
        birth_month=mock_data['month_name'],
        birth_year=mock_data['birth_year'],
        first_name=mock_data['first_name'],
        last_name=mock_data['last_name'],
        address=mock_data['address1'],
        country=mock_data['country'],
        state=mock_data['state'],
        city=mock_data['city'],
        zipcode=mock_data['zipcode'],
        mobile_number=mock_data['mobile_number']
    )

    pages.account_created.account_created_title.wait_to_be_displayed()
    assert (
            pages.account_created.account_created_title.text() ==
            'ACCOUNT CREATED!'
    ), 'Account created title is incorrect'
    assert (
            pages.account_created.account_created_description.text() ==
            'Congratulations! Your new account has been successfully created!'
    ), 'Account created description is incorrect'
