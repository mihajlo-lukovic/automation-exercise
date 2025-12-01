import os
import yaml

from framework.enums import Config


def get_app_config():
    # Get current dir
    root = os.path.dirname(os.path.abspath(__file__))

    # Get project root dir
    project_root = os.path.abspath(os.path.join(root, '..'))

    # Construct config.yaml path from project root
    config_path = os.path.join(
        project_root, Config.DIR.value, Config.CFG.value
    )

    # Load config.yaml
    with open(config_path) as file:
        return yaml.safe_load(file)
