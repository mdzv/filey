# This program monitors a folder for file changes (create, delete, modify, move).

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os

class FileyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        print(f"File moved: from {event.src_path} to {event.dest_path}")

def RunFiley(path_to_watch):
    event_handler = FileyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=True)
    observer.start()

    print(f"Filey is watching: {path_to_watch}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:  
        print("Filey stopped watching.")
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder = os.path.expanduser("~/Desktop") 
    RunFiley(folder)
