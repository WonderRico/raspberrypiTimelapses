import subprocess
import glob
import os.path

ffmpeg = "C:\\Users\\Eric\\Downloads\\ffmpeg-2021-11-22-git-203b0e3561-full_build\\bin\\ffmpeg.exe"
txt = "C:\\Users\\Eric\\Pictures\\timelapse\\ffmpeg_input.txt"
duration = 0.05
camera_folder = os.path.abspath("E:\\Timelapse\\Arquenay\\picam1\\")
#camera_folder = os.path.abspath("\\\\Freebox_Server\\Disque 1\\Photos\\Timelapse\\picam1\\")
date_folders = glob.glob(camera_folder + "/*")

for date_folder in date_folders:
    splited = date_folder.split("\\")
    date = splited[-1]
    try:
        os.remove(txt)
    except FileNotFoundError:
        print()

    video = "E:\\Timelapse\\Videos\\" + date + ".mp4"

    if not os.path.isfile(video):

        filenames = glob.glob(date_folder + '\\*.jpg')
        filenames.sort()

        with open(txt, "wb") as outfile:
            for filename in filenames:
                outfile.write(f"file '{filename}'\n".encode())
                outfile.write(f"duration {duration}\n".encode())

        command_line = ffmpeg + ' -r 30 -f concat -safe 0 -i ' + txt + ' -c:v h264_nvenc -b:v 10M -pix_fmt yuv420p "' + video + '"'
        print(command_line)

        pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
        output = pipe.read().decode()
        pipe.close()

        outfile.close()
