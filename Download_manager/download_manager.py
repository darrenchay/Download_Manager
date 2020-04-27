from os import path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import zipfile
import os
import time


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return None

        # file sys handler on an action, get all files from src and move them to new_dest
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename

            # Getting file type extension
            file_ext = os.path.splitext(filename)
            ext = file_ext[1]
            ext = ext.lower()

            if os.path.isdir(src):
                file_type = "Folders"
            elif ext == ".txt" or ext == ".ctxt":
                file_type = "Text"
            elif ext == ".pdf" or ext == ".one":
                file_type = "PDF Documents"
            elif ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".svg" or ext == ".bmp" or ext == ".jfif":
                file_type = "Images"
            elif ext == ".docx" or ext == ".odt" or ext == ".doc":
                file_type = "Word Documents"
            elif ext == ".csv" or ext == ".dbf" or ext == ".dif" or ext == ".prn" or ext == ".xls" or ext == ".xlsx" or ext == ".xml":
                file_type = "Excel Documents"
            elif ext == ".pptx" or ext == ".ppt":
                file_type = "Powerpoint"
            elif ext == ".exe" or ext == ".msi":
                file_type = "Application"
            elif ext == ".zip" or ext == ".tar" or ext == ".gz":
                if ext == ".zip":
                    print("extracting", filename)
                    zipfile.ZipFile(src, 'r').extractall(folder_dest + "/Folders" + "/" + file_ext[0])
                    #os.remove(src)
                file_type = "Zipped folders"
            elif ext == ".mp3" or ext == ".wav":
                file_type = "Music"
            elif ext == ".c" or ext == ".h" or ext == ".java" or ext == ".py" or ext == ".pl" or ext == ".xsd" \
                    or ext == ".html" or ext == ".js" or ext == ".l68"\
                    or ext == ".s68" or ext == ".x68" or ext == ".json" or ext == ".jar" or ext == ".class":
                file_type = "Code"
            else:
                file_type = "Other"
                print("file: ", file_ext[0], " ext: ", file_ext[1])

            # Updating type-specific folder
            folder_dest_type = folder_dest + "/" + file_type
            if not path.exists(folder_dest_type):
                os.mkdir(folder_dest_type)

            # Getting timestamp
            # date = os.path.getmtime(src)
            # month_format = time.strftime("%Y-%m", time.gmtime(date))

            full_new_path = folder_dest_type
            # if not path.exists(full_new_path):
            #     os.mkdir(full_new_path)
            #     print("Creating dir: ", full_new_path)

            new_dest = full_new_path + "/" + filename
            if not path.exists(new_dest):
                os.rename(src, new_dest)  # change the current file dir to the new folder dir
            else:
                print("Replacing file: ", src)
                os.remove(new_dest)
                os.rename(src, new_dest)  # change the current file dir to the new folder dir


# Running program
folder_to_track = "/Users/darre/Downloads"
folder_dest = "/Users/darre/OneDrive/Desktop/Download Manager"

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
