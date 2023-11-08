import os
from os import path
from shutil import move

srcFolder = "C:/Users/Eric/Pictures/timelapse/raw/"
destFolder = "C:/Users/Eric/Pictures/timelapse/splited/"
if not path.exists(destFolder):
    os.mkdir(destFolder)

for file in os.listdir(os.fsencode(srcFolder)):
    filename = os.fsdecode(file)
    splited = filename.split("_")
    date = splited[0]

    if not path.exists(destFolder + date):
        os.mkdir(destFolder + date)

    dst = destFolder + date + "/" + filename
    move(srcFolder + filename, dst)
