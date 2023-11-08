from datetime import datetime, timedelta
from suntime import Sun, SunTimeException
from os import path
import os
import pytz

home_folder = "/home/pi/pics/"

utc = pytz.timezone("Europe/Paris")

# Arquenay
latitude = 47.99
longitude = -0.57

now = utc.localize(datetime.now())
current_time = now.strftime("%H-%M")
current_day = now.strftime("%Y-%m-%d")
tag = current_day + "_" + current_time

day_folder = home_folder + current_day

if not path.exists(day_folder):
    os.mkdir(day_folder)

sun = Sun(latitude, longitude)
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()

end_night = today_sr - timedelta(minutes=30)
start_night = today_ss + timedelta(hours=1)

if end_night < now < start_night:
    file = "{}/{}.jpg".format(day_folder, tag)
    cmd = "raspistill -o {} -ex auto -awb sun -q 10"
else:
    file = "{}/{}_nuit.jpg".format(day_folder, tag)
    cmd = "raspistill -o {} -awb sun -ss 30000000 -q 10"

os.system(cmd.format(file))

cmd = 'curl --user freebox:Buckny10 --ftp-create-dirs --upload-file {} "ftp://mafreebox.freebox.fr/Disque 1/Photos/Timelapse/picam1/{}/"'
os.system(cmd.format(file, current_day))

cmd = "rm -f {}"
os.system(cmd.format(file))
