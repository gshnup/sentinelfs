import os
import time
import yaml

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from logger import setup_logger

PROTECTED_DIR = "protected"
CONFIG_FILE = "config/policy.yaml"

logger = setup_logger()


def load_policy():

    with open(CONFIG_FILE, "r") as file:
        config = yaml.safe_load(file)

    return set(config.get("allowed_files", []))


ALLOWED_FILES = load_policy()


class SentinelHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)

        logger.info(f"Detected new file: {filename}")

        if filename not in ALLOWED_FILES:

            logger.warning(f"Unauthorized file detected: {filename}")

            os.remove(event.src_path)

            logger.warning(f"Deleted unauthorized file: {filename}")

        else:
            logger.info(f"Allowed file detected: {filename}")


if __name__ == "__main__":

    event_handler = SentinelHandler()

    observer = Observer()

    observer.schedule(event_handler, PROTECTED_DIR, recursive=True)

    observer.start()

    logger.info("SentinelFS monitoring started")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

        logger.info("SentinelFS stopped")

    observer.join()
