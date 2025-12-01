from datetime import datetime, date
from pathlib import Path

import pytest
from faker import Faker

from clients.public_api import PublicAPI
from framework.driver import Driver
from framework.enums import MockStatic


@pytest.fixture
def driver():
    driver = Driver()
    driver.init_browser()

    yield driver

    driver.quit_browser()


@pytest.fixture
def mock_data():
    fake = Faker()

    # Create unique email
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    base_email = fake.email()
    unique_email = f'{timestamp}{base_email}'

    # Convert birth_day to eliminate beginning zero
    birth_day = int(fake.day_of_month())
    birth_day = str(birth_day)

    # Modify birth_year
    five_years_ago = date.today().replace(year=date.today().year - 5)
    birth_year = str(fake.date_between(end_date=five_years_ago).year)

    return {
        'name': fake.first_name(),
        'email': unique_email,
        'description': fake.text(),
        'subject': fake.sentence(),
        'password': fake.password(),
        'title': MockStatic.TITLE.value,
        'birth_date': birth_day,
        'birth_month': fake.month(),
        'month_name': fake.month_name(),
        'birth_year': birth_year,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'address1': fake.address(),
        'country': MockStatic.COUNTRY.value,
        'state': fake.state(),
        'city': fake.city(),
        'zipcode': fake.zipcode(),
        'mobile_number': fake.phone_number()
    }


@pytest.fixture
def api_client():
    return PublicAPI()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed and report.when == 'call':
        driver = item.funcargs.get('driver', None)
        if driver is not None:
            parent_dir: str = 'screenshots'

            # Get project root
            project_root = Path(__file__).resolve().parent.parent

            # Create screenshots dir
            screenshots_dir = project_root / parent_dir
            screenshots_dir.mkdir(exist_ok=True)

            # Generate screenshot name
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            file_name = f'{item.name.replace('/', '-')}_{timestamp}.png'
            file_path = screenshots_dir / file_name

            # Save screenshot
            driver.driver.save_screenshot(file_path)
