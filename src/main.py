import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

PROTECTED_DIR = "protected"

ALLOWED_FILES = {
    "allowed.txt"
}



class SentinelHandler (FileSystemEventHandler):


    def on_created(self, event):

        if event.is_directory:
           return


        filename = os.path.basename(event.src_path)

        print(f"[+] Detected new file: {filename}")

        if filename not in ALLOWED_FILES:

           print(f"[!] Unauthorized file detected: {filename}")

           os.remove(event.src_path)
    
           print(f"[-] Deleted: {filename}")



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
