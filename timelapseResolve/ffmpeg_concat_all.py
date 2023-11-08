import glob
import os.path
import subprocess

ffmpeg = "C:\\Users\\Eric\\Downloads\\ffmpeg-2021-11-22-git-203b0e3561-full_build\\bin\\ffmpeg.exe"
txt = "C:\\Users\\Eric\\Pictures\\timelapse\\ffmpeg_input.txt"
duration = 0.05
dailys_folder = os.path.abspath("C:\\Users\\Eric\Videos\\timelapse\\")
filenames = glob.glob(dailys_folder + '\\*.mp4')
first = filenames[0].split("\\")[-1].split(".")[0]
last = filenames[-1].split("\\")[-1].split(".")[0]
output = dailys_folder + "_CONCAT_" + first + "_to_" + last + ".mp4"

if not os.path.isfile(output):

    try:
        os.remove(txt)
    except FileNotFoundError:
        print()

    with open(txt, "wb") as outfile:
        for filename in filenames:
            outfile.write(f"file '{filename}'\n".encode())

    command_line = ffmpeg + " -f concat -safe 0 -i " + txt + " -c copy " + output
    print(command_line)

    pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE).stdout
    output = pipe.read().decode()
    pipe.close()
