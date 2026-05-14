import os

from watchdog.events import FileSystemEventHandler

from policy import load_policy
from enforcer import delete_file
from logger import setup_logger

logger = setup_logger()

ALLOWED_FILES = load_policy()


class SentinelHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        filename = os.path.basename(event.src_path)

        logger.info(f"Detected new file: {filename}")

        if filename not in ALLOWED_FILES:

            logger.warning(f"Unauthorized file detected: {filename}")

            delete_file(event.src_path)

            logger.warning(f"Deleted unauthorized file: {filename}")

        else:
            logger.info(f"Allowed file detected: {filename}")
