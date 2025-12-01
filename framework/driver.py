import os

from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from framework.enums import Execution, EnvVariables

run_env = Execution.CI.value if os.getenv(
    Execution.ACTIONS.value
) == "true" else Execution.LOCAL.value


class Driver:

    def __init__(self):
        self.driver = None

        if run_env == Execution.LOCAL.value:
            load_dotenv()

    @classmethod
    def get_driver(cls):
        env_variables = os.environ

        if EnvVariables.DRIVER.value not in os.environ:
            raise NameError('Driver not specified in root .env')

        return Service(
            executable_path=env_variables[EnvVariables.DRIVER.value]
        )

    def init_browser(self):
        if run_env == Execution.LOCAL.value:
            self.driver = webdriver.Chrome(
                service=self.get_driver(),
                options=webdriver.ChromeOptions()
            )
        else:
            options = Options()

            # Additional options for CI
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')

            self.driver = webdriver.Chrome(options=options)

        self.driver.maximize_window()

    def quit_browser(self):
        self.driver.quit()
