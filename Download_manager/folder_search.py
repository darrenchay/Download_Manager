from os import path
import os

for folderName in os.listdir("/Users/darre/OneDrive/Desktop/Download Manager"):
    pathName = "/Users/darre/OneDrive/Desktop/Download Manager" + "/" + folderName
    for subFolder in os.listdir("/Users/darre/OneDrive/Desktop/Download Manager" + "/" + folderName):
        print("subfolder:", subFolder, "path: ", pathName)
        filePath = "/Users/darre/OneDrive/Desktop/Download Manager" + "/" + folderName + "/" + subFolder
        if os.path.isdir(filePath):
            for filename in os.listdir(filePath):
                src = filePath + "/" + filename
                print(src)

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
                    file_type = "Unzipped folders"
                elif ext == ".mp3" or ext == ".wav":
                    file_type = "Music"
                elif ext == ".c" or ext == ".h" or ext == ".java" or ext == ".py" or ext == ".pl" or ext == ".xsd" \
                        or ext == ".html" or ext == ".js" or ext == ".l68" \
                        or ext == ".s68" or ext == ".x68" or ext == ".json" or ext == ".jar" or ext == ".class":
                    file_type = "Code"
                else:
                    file_type = "Other"
                    print("file: ", file_ext[0], " ext: ", file_ext[1])

                # Updating type-specific folder
                dest = "/Users/darre/OneDrive/Desktop/Download Manager"
                folder_dest_type = dest + "/" + file_type
                print(folder_dest_type)
                if not path.exists(folder_dest_type):
                    os.mkdir(folder_dest_type)

                full_new_path = folder_dest_type

                new_dest = full_new_path + "/" + filename
                if not path.exists(new_dest):
                    os.rename(src, new_dest)  # change the current file dir to the new folder dir


print("done")
