import os
from shutil import move

srcFolder = "C:/Users/Eric/Pictures/timelapse/bridge/"
destFolder = "C:/Users/Eric/Pictures/timelapse/resolve/"

i = 0
for file in os.listdir(os.fsencode(srcFolder)):
    filename = os.fsdecode(file)
    if filename.endswith("jpeg") or filename.endswith("jpg"):
        print(filename)
        dst = destFolder + str(i) + ".jpg"
        move(srcFolder + filename, dst)
        i += 1
