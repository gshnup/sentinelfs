import os
import time
import yaml

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PROTECTED_DIR = "protected"
CONFIG_FILE = "config.yaml"


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

        print(f"[+] Detected: {filename}")

        if filename not in ALLOWED_FILES:

            print(f"[!] Unauthorized file: {filename}")

            os.remove(event.src_path)

            print(f"[-] Deleted: {filename}")

        else:
            print(f"[✓] Allowed file: {filename}")


if __name__ == "__main__":

    event_handler = SentinelHandler()

    observer = Observer()

    observer.schedule(event_handler, PROTECTED_DIR, recursive=True)

    observer.start()

    print("[SentinelFS] Monitoring started...")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()
