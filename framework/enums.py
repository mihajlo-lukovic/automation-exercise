import enum


class Execution(enum.Enum):

    LOCAL = 'LOCAL'
    CI = 'CI'
    ACTIONS = 'GITHUB_ACTIONS'


class EnvVariables(enum.Enum):

    DRIVER = 'DRIVER'


class Actions(enum.Enum):

    TIMEOUT = 10


class Config(enum.Enum):

    DIR = 'application'
    CFG = 'config.yaml'


class MockStatic(enum.Enum):

    TITLE = 'Mr.'
    COUNTRY = 'United States'
