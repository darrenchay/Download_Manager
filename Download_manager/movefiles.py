import os

src = "/Users/darre/OneDrive/Desktop/Download Manager/Unzipped folders"
for file in os.listdir(src):
    print(file)
    newName = file.split(".zip")
    print()
    print(newName[0])
    os.rename(src + "/" + file, src + "/" + newName[0])

