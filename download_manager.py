from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return None

        # file sys handler on an action, get all files from src and move them to new_dest
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_dest = folder_dest + "/" + filename
            os.rename(src, new_dest)  # change the current file dir to the new folder dir
            print("moving: ", filename, " to", new_dest)

        # elif event.event_type == 'created':
        #     # Event is created, you can process it now
        #     print("Watchdog received created event - % s." % event.src_path)
        # elif event.event_type == 'modified':
        #     # Event is modified, you can process it now
        #     print("Watchdog received modified event - % s." % event.src_path)


# Running program
folder_to_track = "/Users/darre/Downloads/testing"
folder_dest = "/Users/darre/Downloads/output"
# os.rename(folder_to_track + "/test.txt", folder_dest + "/newTest.txt")

event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Terminating...")
    observer.stop()
observer.join()
