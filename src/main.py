import time

from watchdog.observers import Observer

from watcher import SentinelHandler
from logger import setup_logger

PROTECTED_DIR = "protected"

logger = setup_logger()


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
