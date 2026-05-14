import yaml

CONFIG_FILE = "config/policy.yaml"


def load_policy():

    with open(CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)

    return set(config.get("allowed_files", []))
